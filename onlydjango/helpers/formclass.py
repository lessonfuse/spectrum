
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

FORM_STYLES = {
    "input": "mt-1 block w-full py-2 focus:outline-none focus:border-black sm:text-sm",
    "textinput": "mt-1 block w-full py-2 focus:outline-none focus:border-black sm:text-sm",
    "textarea": "mt-1 block w-full sm:text-sm border border-black focus:outline-none focus:border-black",
    "file": "absolute w-full h-full opacity-0 cursor-pointer border-black hidden",
    "checkbox": "mt-1 block border border-black p-3 focus:outline-none focus:border-black sm:text-sm",
}


SUBMIT_BUTTON_STYLE = (
    "inline-flex justify-center py-2 px-4 border border-black text-sm "
    "font-bold text-black bg-white hover:bg-gray-100 focus:outline-none"
)


class ODFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_tag = kwargs.get("form_tag", True)
        self.form_method = kwargs.get("form_method", "POST")
        self.form_id = kwargs.get("form_id", "od_form")
        self.form_class = kwargs.get("form_class", "py-6")
        self.label_class = kwargs.get(
            "label_class", "block text-sm font-medium text-gray-700 "
        )
        # self.field_template = "helpers/field.html"

        # Set up CSS styles
        self.field_class = FORM_STYLES["input"]
        for field_type, css_class in FORM_STYLES.items():
            setattr(self, f"{field_type}_class", css_class)

        # Set up layout with submit button
        submit_text = kwargs.get("submit_text", "Save")
        self.add_input(Submit("submit", submit_text, css_class=SUBMIT_BUTTON_STYLE))

    def set_form_action(self, action):
        self.form_action = action

    def set_form_method(self, method):
        self.form_method = method

    def set_form_id(self, form_id):
        self.form_id = form_id

    def set_form_class(self, form_class):
        self.form_class = form_class

    def set_label_class(self, label_class):
        self.label_class = label_class
