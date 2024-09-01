"""
To be used with crispy tailwind along with the {% crispy %} tag.

With Django Generic views that take a form you can simply pass the helper and in the template you would generally have:

# generic/create.html
{% block base_content %}
    <div class="container mx-auto px-4 py-4 rounded-xl">
        <h2 class="text-2xl font-semibold text-gray-900">
            {{ title }}
        </h2>
       {% crispy form helper %}
    </div>
{% endblock %}

# appname/views.py
@method_decorator(user_passes_test(is_admin), name="dispatch")
class ObjectCreateView(ODCreateView):
    model = Object
    fields = [
        "first_name",
        "last_name",
        "bio",
        "phone_number",
    ]
    success_url = reverse_lazy("admin_doctor_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Object"
        context["back_url"] = reverse("admin_object_list")
        return context

# helpers/cbv.py

class ODCreateView(CreateView):
    template_name = "generic/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["helper"] = CareOneFormHelper()
        
        return context
"""

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

FORM_STYLES = {
    "input": "mt-1 block w-full rounded-md py-2 focus:outline-none focus:ring-sky-500 focus:border-sky-500 sm:text-sm",
    "textarea": "shadow-sm focus:ring-sky-500 focus:border-sky-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md",
    "file": "absolute w-full h-full opacity-0 cursor-pointer border-gray-300 rounded-md hidden",
    "checkbox": "mt-1 block border border-gray-300 rounded-md shadow-sm p-3 focus:outline-none focus:ring-sky-500 focus:border-sky-500 sm:text-sm",
}


SUBMIT_BUTTON_STYLE = (
    "inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm "
    "font-medium rounded-md text-white bg-sky-600 hover:bg-sky-700 focus:outline-none "
    "focus:ring-2 focus:ring-offset-2 focus:ring-sky-500"
)


class ODFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_tag = kwargs.get("form_tag", False)
        self.form_method = kwargs.get("form_method", "POST")
        self.form_id = kwargs.get("form_id", "care_one_form")
        self.form_class = kwargs.get("form_class", "py-6 ")
        self.label_class = kwargs.get(
            "label_class", "block text-sm font-medium text-gray-700 "
        )

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
