# import pynecone

# # Define the form steps
# steps = [
#     {
#         "title": "Company information",
#         "fields": [
#             {
#                 "name": "company_name",
#                 "label": "Company name",
#                 "type": "text"
#             },
#             {
#                 "name": "mission_statement",
#                 "label": "Mission statement",
#                 "type": "textarea"
#             }
#         ]
#     },
#     {
#         "title": "Lyrics",
#         "fields": [
#             {
#                 "name": "lyrics",
#                 "label": "Lyrics",
#                 "type": "textarea"
#             }
#         ]
#     },
#     {
#         "title": "Musical style",
#         "fields": [
#             {
#                 "name": "musical_style",
#                 "label": "Musical style",
#                 "type": "select",
#                 "options": [
#                     "Christmas",
#                     "Classical",
#                     "Electronic",
#                     "Pop",
#                     "Urban",
#                     "Rock"
#                 ]
#             }
#         ]
#     },
#     {
#         "title": "Jingle",
#         "fields": [
#             {
#                 "name": "jingle",
#                 "label": "Jingle",
#                 "type": "audio"
#             }
#         ]
#     }
# ]

# # Create the form
# form = pynecone.Form(steps)

# # Display the form
# form.display()


import pynecone as pc


class State(pc.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return pc.hstack(
        pc.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=State.decrement,
        ),
        pc.heading(State.count, font_size="2em"),
        pc.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=State.increment,
        ),
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()