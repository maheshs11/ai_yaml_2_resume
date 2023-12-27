import cairo


def page1(surface: cairo.Surface, yaml_out) -> None:
    context = cairo.Context(surface)

    # Set A4 margins
    margin_x, margin_y = 20, 20

    # set page centre
    page_center = 250

    # Define colors
    header_color = (0.247, 0.247, 0.247)  # Dark gray
    text_color = (0.9, 0.0, 0.0)  # Black
    line_color = (0.737, 0.737, 0.737)  # Light gray

    # Set fonts
    title_font = ('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    main_text_font = ('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    section_title_font = ('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

    # Draw header section
    # context.set_source_rgb(*header_color)
    # context.rectangle(margin_x, margin_y, 210 - 2 * margin_x, 40)
    # context.fill()

    # Draw name
    context.set_source_rgb(*text_color)
    context.select_font_face(*title_font)
    context.set_font_size(24)
    context.move_to(page_center -30, margin_y + 20)
    context.show_text(yaml_out.get('basic').get('name', ''))

    # Draw designation
    context.set_source_rgb(*text_color)
    context.select_font_face(*title_font)
    context.set_font_size(14)
    context.move_to(page_center -50 , margin_y + 40)
    context.show_text(yaml_out.get('basic').get('role', ''))

    # Draw email and phone number
    context.select_font_face(*main_text_font)
    context.set_font_size(12)
    context.move_to(margin_x + 30, margin_y + 60)
    context.show_text(yaml_out.get('basic').get('contact', '').get('email', ''))
    context.show_text("  ")
    context.show_text(yaml_out.get('basic').get('contact', '').get('phone', ''))
    context.show_text("  ")
    context.show_text(yaml_out.get('basic').get('contact', '').get('address', ''))
    context.show_text("  ")
    #context.show_text(yaml_out.get('basic').get('websites', '').get('text', ''))

    # Draw horizontal line
    # context.set_source_rgb(*line_color)
    # context.move_to(margin_x, margin_y + 60)
    # context.line_to(210 - margin_x, margin_y + 60)
    # context.stroke()

    # Draw profile section title
    context.select_font_face(*section_title_font)
    context.set_font_size(14)
    context.move_to(page_center -30, margin_y + 85)
    context.show_text("Profile")

    # Draw remaining text blocks (replace with your actual content)
    context.select_font_face(*main_text_font)
    context.set_font_size(12)
    # Set spacing
    line_height = 25

    text = yaml_out.get('profile', '')
    # Draw text with line breaks
    x, y = 50, 140
    for line in text.split('\n'):
        context.move_to(x, y)
        context.show_text(line)
        y += line_height


def page2(surface: cairo.Surface, yaml_out) -> None:
    context = cairo.Context(surface)
