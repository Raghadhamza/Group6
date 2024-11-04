import ifcopenshell

def identify_curtain_walls(model):
    curtain_walls = model.by_type('IfcCurtainWall')
    result = f"Curtain Walls: {len(curtain_walls)}"
    return curtain_walls, result
