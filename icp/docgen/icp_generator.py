from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from PIL import Image as PILImage

class ICPDocumentGenerator:
    def __init__(self, student):
        self.student = student
        self.buffer = BytesIO()
        self.document = SimpleDocTemplate(self.buffer, pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.elements = []

    def generate(self):
        self._add_logo_and_header()
        self._add_student_info_table()
        self._add_parents_concern()
        self._add_medical_alerts()
        self._add_complex_learning_profile()
        self._add_focus_developmental_areas()
        self._add_skills_strengths()
        self._add_present_levels_of_performance()
        self._add_goals()
        self._add_intervention_services()
        self._add_supplementary_services()
        self._add_meeting_participants()
        
        self.document.build(self.elements)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf

    def _add_logo_and_header(self):
        if self.student.school_logo:
            logo = PILImage.open(BytesIO(self.student.school_logo.read()))
            logo_width = 2.5 * inch
            logo_height = logo_width * (logo.height / logo.width)
            img = Image(BytesIO(self.student.school_logo.read()), width=logo_width, height=logo_height)
            self.elements.append(img)

        header_style = ParagraphStyle(name='Header', parent=self.styles['Heading1'], alignment=1)
        header = Paragraph('INDIVIDUALIZED CURRICULUM PLAN', header_style)
        self.elements.append(header)
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_student_info_table(self):
        data = [
            ['Name', self.student.name],
            ['ID Card Number', self.student.id_card_number],
            ['Age', str(self.student.age)],
            ['IE Program', self.student.ie_program],
            ['Index', self.student.index],
            ['Date', str(self.student.date_of_document)]
        ]
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_parents_concern(self):
        self.elements.append(Paragraph('Parents Concern', self.styles['Heading2']))
        self.elements.append(Paragraph(self.student.general_information.parent_concerns, self.styles['Normal']))
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_medical_alerts(self):
        self.elements.append(Paragraph('Medical Alerts, Background and History', self.styles['Heading2']))
        self.elements.append(Paragraph(self.student.general_information.medical_alerts, self.styles['Normal']))
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_complex_learning_profile(self):
        self.elements.append(Paragraph('Complex Learning Profile', self.styles['Heading2']))
        learning_profile = self.student.learning_profile
        data = []
        for field in learning_profile._meta.get_fields():
            if field.name not in ['id', 'student']:
                value = getattr(learning_profile, field.name)
                data.append([field.verbose_name, dict(learning_profile.CONDITION_STATUS)[value] if isinstance(value, str) else str(value)])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_focus_developmental_areas(self):
        self.elements.append(Paragraph('Focus Developmental and Learning Areas', self.styles['Heading2']))
        dev_areas = self.student.developmental_area
        data = []
        for field in dev_areas._meta.get_fields():
            if field.name not in ['id', 'student']:
                value = getattr(dev_areas, field.name)
                data.append([field.verbose_name, 'Yes' if value else 'No' if isinstance(value, bool) else str(value)])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_skills_strengths(self):
        self.elements.append(Paragraph('Student Skills & Strengths', self.styles['Heading2']))
        skills = self.student.skills_strengths
        for field in skills._meta.get_fields():
            if field.name not in ['id', 'student']:
                self.elements.append(Paragraph(f'{field.verbose_name}: {getattr(skills, field.name)}', self.styles['Normal']))
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_present_levels_of_performance(self):
        self.elements.append(Paragraph('Present Levels of Educational Performance', self.styles['Heading2']))
        # Add code to include present levels of performance data
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_goals(self):
        self.elements.append(Paragraph('Goals', self.styles['Heading2']))
        goals = self.student.goals.all()
        for goal in goals:
            data = []
            for field in goal._meta.get_fields():
                if field.name not in ['id', 'student']:
                    data.append([field.verbose_name, str(getattr(goal, field.name))])
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            self.elements.append(table)
            self.elements.append(Spacer(1, 0.25*inch))

    def _add_intervention_services(self):
        self.elements.append(Paragraph('Intervention Services', self.styles['Heading2']))
        services = self.student.intervention_services.all()
        data = [['Program', 'Frequency', 'Duration', 'Location', 'Initiation Date']]
        for service in services:
            data.append([service.program, service.frequency, service.duration, service.location, str(service.initiation_date)])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_supplementary_services(self):
        self.elements.append(Paragraph('Supplementary Services', self.styles['Heading2']))
        services = self.student.supplementary_services.all()
        data = [['Type of Support', 'Time', 'Duration']]
        for service in services:
            data.append([service.type_of_support, service.time, service.duration])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.25*inch))

    def _add_meeting_participants(self):
        self.elements.append(Paragraph('ICP Meeting Participants', self.styles['Heading2']))
        participants = self.student.icp_participants.all()
        data = [['Name', 'Designation', 'Signature', 'Date']]
        for participant in participants:
            data.append([participant.name, participant.designation, participant.signature, str(participant.date)])
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        self.elements.append(table)
