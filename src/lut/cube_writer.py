def write_cube(path, title, lut_size, lut_table):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'TITLE "{title}"\n')
        f.write(f"LUT_3D_SIZE {lut_size}\n")
        f.write("DOMAIN_MIN 0.0 0.0 0.0\n")
        f.write("DOMAIN_MAX 1.0 1.0 1.0\n\n")

        for r, g, b in lut_table:
            f.write(f"{r:.6f} {g:.6f} {b:.6f}\n")