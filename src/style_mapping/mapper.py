from models import StyleParameters

def apply_parsed_rules(parsed_rules):
    params = StyleParameters.neutral()

    for rule in parsed_rules:
        intensity = rule["intensity"]

        if rule["temperature"] is not None:
            params.temperature += rule["temperature"] * intensity

        if rule["contrast"] is not None:
            params.contrast *= rule["contrast"]

        if rule["saturation"] is not None:
            params.saturation *= rule["saturation"]

        if rule["color"] is not None:
            r, g, b = rule["color"]
            if rule["region"] == "shadows":
                params.shadows_rgb = (
                    params.shadows_rgb[0] + r * intensity,
                    params.shadows_rgb[1] + g * intensity,
                    params.shadows_rgb[2] + b * intensity
                )
            
            elif rule["region"] == "highlights":
                params.highlights_rgb = (
                    params.highlights_rgb[0] + r * intensity,
                    params.highlights_rgb[1] + g * intensity,
                    params.highlights_rgb[2] + b * intensity
                )
            else:
                params.midtones_rgb = (
                    params.midtones_rgb[0] + r * intensity,
                    params.midtones_rgb[1] + g * intensity,
                    params.midtones_rgb[2] + b * intensity,
                )
    
    return params