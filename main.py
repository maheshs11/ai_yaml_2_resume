#!/usr/bin/env python3
from io import BytesIO
from pathlib import Path
import cairo
import yaml
from nicegui import ui
import os
from dotenv import load_dotenv
from template import page1, page2
# Load variables from .env file
load_dotenv()

# Access the variable
my_variable = os.getenv("MY_VARIABLE")

# Now 'my_variable' contains the value from the .env file
print(my_variable)

# A4 dimensions in points (1 inch = 72 points)
# a4_width_points = 595.276
# a4_height_points = 841.890

PDF_PATH = Path('resume.pdf')


def generate_svg1(yaml_out) -> str:
    output = BytesIO()
    surface = cairo.SVGSurface(output, 550, 800)
    page1(surface, yaml_out)
    surface.finish()
    return output.getvalue().decode('utf-8')


def generate_svg2(yaml_out) -> str:
    output = BytesIO()
    surface = cairo.SVGSurface(output, 550, 800)
    page2(surface, yaml_out)
    surface.finish()
    return output.getvalue().decode('utf-8')


def generate_pdf(yaml_out) -> bytes:
    output = BytesIO()
    surface = cairo.PDFSurface(output, 550, 800)
    page1(surface, yaml_out)
    surface.show_page()
    page2(surface, yaml_out)
    surface.finish()
    return output.getvalue()



def string_to_yaml_with_pyyaml(input_string):
    try:
        yaml_data = yaml.safe_load(input_string)
        # print('type_yaml_to_dict', type(yaml_data))
        # yaml_output = yaml.dump(yaml_data)
        return yaml_data
    except yaml.YAMLError as e:
        return f"Error converting string to YAML_dict: {e}"


def parse_yaml(e):
    text = e.content.read().decode('utf-8')
    # print(text)
    yaml_out = string_to_yaml_with_pyyaml(text)
    # print(yaml_out.get('experiencs'))
    # print(yaml_out[].basic, type(yaml_out))
    preview1.content = generate_svg1(yaml_out)
    preview2.content = generate_svg2(yaml_out)
    PDF_PATH.write_bytes(generate_pdf(yaml_out))

with ui.header():
    ui.label("AI yaml to resume pdf converter").classes('max-w-full')

with ui.left_drawer():
    Yaml_PATH = "raw_resume_example.yaml"
    ui.button('Download sample .yaml resume to modify', on_click=lambda: ui.download(Yaml_PATH))

with ui.column():
    resume = ui.upload(label='sample.yaml', auto_upload=True, on_upload=parse_yaml).props('accept=.yaml,.yml').classes(
        'max-w-full')
    ui.button('Download PDF', on_click=lambda: ui.download(PDF_PATH))
    preview1 = ui.html().classes('border-2 border-gray-500')
    preview2 = ui.html().classes('border-2 border-gray-500')

ui.run()
