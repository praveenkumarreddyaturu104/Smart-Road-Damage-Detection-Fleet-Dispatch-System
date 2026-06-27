import os
import xml.etree.ElementTree as ET

# ==========================================
# CONFIGURATION
# ==========================================

CLASS_MAP = {
    "D00": 0,  # Longitudinal Crack
    "D10": 1,  # Transverse Crack
    "D20": 2,  # Alligator Crack
    "D40": 3   # Pothole
}

XML_DIR = r"train/Japan/annotations"
OUTPUT_DIR = r"train/Japan/labels"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# START CONVERSION
# ==========================================

converted = 0
skipped = 0

for xml_file in os.listdir(XML_DIR):

    if not xml_file.endswith(".xml"):
        continue

    xml_path = os.path.join(XML_DIR, xml_file)

    try:

        tree = ET.parse(xml_path)
        root = tree.getroot()

        width_elem = root.find("size/width")
        height_elem = root.find("size/height")

        if width_elem is None or height_elem is None:
            skipped += 1
            continue

        if width_elem.text is None or height_elem.text is None:
            skipped += 1
            continue

        width = int(width_elem.text)
        height = int(height_elem.text)

        objects = root.findall("object")

        if len(objects) == 0:
            skipped += 1
            continue

        yolo_lines = []

        for obj in objects:

            name_elem = obj.find("name")

            if name_elem is None:
                continue

            if name_elem.text is None:
                continue

            cls_name = str(name_elem.text)

            if cls_name not in CLASS_MAP:
                continue

            cls_id = CLASS_MAP[cls_name]

            bbox = obj.find("bndbox")

            if bbox is None:
                continue

            xmin_elem = bbox.find("xmin")
            ymin_elem = bbox.find("ymin")
            xmax_elem = bbox.find("xmax")
            ymax_elem = bbox.find("ymax")

            if (
                xmin_elem is None or
                ymin_elem is None or
                xmax_elem is None or
                ymax_elem is None
            ):
                continue

            if (
                xmin_elem.text is None or
                ymin_elem.text is None or
                xmax_elem.text is None or
                ymax_elem.text is None
            ):
                continue

            xmin = float(str(xmin_elem.text))
            ymin = float(str(ymin_elem.text))
            xmax = float(str(xmax_elem.text))
            ymax = float(str(ymax_elem.text))

            x_center = ((xmin + xmax) / 2) / width
            y_center = ((ymin + ymax) / 2) / height

            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            yolo_lines.append(
                f"{cls_id} "
                f"{x_center:.6f} "
                f"{y_center:.6f} "
                f"{box_width:.6f} "
                f"{box_height:.6f}"
            )

        if len(yolo_lines) == 0:
            skipped += 1
            continue

        txt_name = xml_file.replace(".xml", ".txt")

        txt_path = os.path.join(
            OUTPUT_DIR,
            txt_name
        )

        with open(txt_path, "w") as f:
            f.write("\n".join(yolo_lines))

        converted += 1

    except Exception as e:
        print(f"Error processing {xml_file}: {e}")
        skipped += 1

print("\n==============================")
print("XML → YOLO Conversion Complete")
print("==============================")
print(f"Converted Files : {converted}")
print(f"Skipped Files   : {skipped}")
print("==============================")