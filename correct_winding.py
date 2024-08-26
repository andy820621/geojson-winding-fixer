import json
from shapely.geometry import Polygon, MultiPolygon, mapping, shape
from shapely.ops import orient

def ensure_ccw(coords):
    poly = Polygon(coords)
    if not poly.exterior.is_ccw:
        return list(poly.exterior.coords)[::-1]
    return list(poly.exterior.coords)

def fix_polygon(coords):
    if not coords:
        return coords
    if coords[0] != coords[-1]:
        coords.append(coords[0])
    coords = ensure_ccw(coords)
    return coords[:-1]  # 移除重複的閉合點

def fix_multipolygon(multi_coords):
    if isinstance(multi_coords[0], (int, float)):
        return [fix_polygon(multi_coords)]
    
    fixed_polys = []
    for poly_coords in multi_coords:
        if isinstance(poly_coords[0], (int, float)):
            fixed_poly = fix_polygon(poly_coords)
        else:
            fixed_poly = fix_polygon(poly_coords[0])
            holes = [fix_polygon(hole) for hole in poly_coords[1:]]
            fixed_poly = [fixed_poly] + holes
        fixed_polys.append(fixed_poly)
    return fixed_polys

def fix_geojson(geojson_data):
    for feature in geojson_data['features']:
        geom = feature['geometry']
        if geom['type'] == 'Polygon':
            geom['coordinates'] = [fix_polygon(geom['coordinates'][0])]
        elif geom['type'] == 'MultiPolygon':
            geom['coordinates'] = fix_multipolygon(geom['coordinates'])
        
        # 使用 shapely 的 shape 和 mapping 函數來進一步確保幾何形狀的有效性
        fixed_shape = shape(geom)
        if not fixed_shape.is_valid:
            fixed_shape = fixed_shape.buffer(0)
        fixed_shape = orient(fixed_shape)  # 確保遵循右手規則
        feature['geometry'] = mapping(fixed_shape)
    
    return geojson_data

# 讀取 GeoJSON 文件
with open('input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 修正 GeoJSON
fixed_data = fix_geojson(data)

# 將修正後的 GeoJSON 寫入新文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_data, f, ensure_ascii=False, indent=2)

print("GeoJSON 已修正並保存為 output.json")
