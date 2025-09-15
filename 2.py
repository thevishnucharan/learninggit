import tkinter as tk
from tkinter import ttk, filedialog, simpledialog
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable, Image


class HorizontalLine(Flowable):
    """A custom horizontal line for separating sections."""
    def __init__(self, width=500, thickness=1, color=colors.black):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.color = color

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


def create_pdf(name, email, phone, about, education, skills, cert, link, interests, job_history, photo_path, pdf_filename):
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle', parent=styles['Title'], fontName='Helvetica-Bold',
        fontSize=18, spaceAfter=12, textColor=colors.blue
    )

    heading1_style = ParagraphStyle(
        'Heading1Style', parent=styles['Heading1'], fontName='Helvetica-Bold',
        fontSize=14, spaceBefore=12, spaceAfter=6, textColor=colors.darkblue
    )

    normal_style = ParagraphStyle(
        'NormalStyle', parent=styles['Normal'], fontName='Helvetica',
        fontSize=10, spaceBefore=5, spaceAfter=5, textColor=colors.black
    )

    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    content = []

    # Add Photo if available
    if photo_path:
        content.append(Image(photo_path, width=100, height=100))
        content.append(Spacer(1, 12))

    # Personal Information (Name, Email, and Phone in one line)
    content.append(Paragraph(name, title_style))
    personal_info = f"{email} | {phone}"
    content.append(Paragraph(personal_info, normal_style))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # About Section
    content.append(Paragraph('<b>About:</b>', heading1_style))
    content.append(Paragraph(about, normal_style))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # Education
    content.append(Paragraph('<b>Education:</b>', heading1_style))
    for edu in education:
        content.append(Paragraph(f"{edu[0]} ({edu[1]})", normal_style))
        content.append(Paragraph(f"Duration: {edu[2]}", normal_style))
        content.append(Spacer(1, 6))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # Skills
    content.append(Paragraph('<b>Skills:</b>', heading1_style))
    for skill in skills:
        content.append(Paragraph(skill.strip(), normal_style))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # Certificates
    content.append(Paragraph('<b>Certificates:</b>', heading1_style))
    for c in cert:
        content.append(Paragraph(c.strip(), normal_style))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # Links
    content.append(Paragraph('<b>Links:</b>', heading1_style))
    for l in link:
        content.append(Paragraph(l.strip(), normal_style))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # Interests
    content.append(Paragraph('<b>Interests:</b>', heading1_style))
    for interest in interests:
        content.append(Paragraph(interest.strip(), normal_style))
    content.append(Spacer(1, 12))
    content.append(HorizontalLine())
    content.append(Spacer(1, 12))

    # Job Experience
    content.append(Paragraph('<b>Experience:</b>', heading1_style))
    for job in job_history:
        content.append(Paragraph(f"{job[0]} - {job[1]}", normal_style))
        content.append(Paragraph(f"Duration: {job[2]}", normal_style))
        content.append(Paragraph(job[3], normal_style))
        content.append(Spacer(1, 6))
    content.append(Spacer(1, 12))

    doc.build(content)


class ResumeBuilderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Resume Builder")

        # GUI Elements
        self.name_label = ttk.Label(master, text="Full Name:")
        self.name_entry = ttk.Entry(master)
        self.email_label = ttk.Label(master, text="Email:")
        self.email_entry = ttk.Entry(master)
        self.phone_label = ttk.Label(master, text="Phone:")
        self.phone_entry = ttk.Entry(master)
        self.about_label = ttk.Label(master, text="About:")
        self.about_text = tk.Text(master, height=5, width=30)
        self.photo_button = ttk.Button(master, text="Upload Photo", command=self.upload_photo)
        self.add_edu_button = ttk.Button(master, text="Add Education", command=self.add_education)
        self.add_job_button = ttk.Button(master, text="Add Job", command=self.add_job)
        self.add_skill_button = ttk.Button(master, text="Add Skill", command=self.add_skill)
        self.add_cert_button = ttk.Button(master, text="Add Certificate", command=self.add_certificate)
        self.add_link_button = ttk.Button(master, text="Add Link", command=self.add_link)
        self.add_interest_button = ttk.Button(master, text="Add Interest", command=self.add_interest)
        self.save_button = ttk.Button(master, text="Save Resume", command=self.save_resume)

        # Layout
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry.grid(row=0, column=1)
        self.email_label.grid(row=0, column=2, sticky="e")
        self.email_entry.grid(row=0, column=3)
        self.phone_label.grid(row=0, column=4, sticky="e")
        self.phone_entry.grid(row=0, column=5)
        self.about_label.grid(row=1, column=0, sticky="e")
        self.about_text.grid(row=1, column=1, columnspan=5)
        self.photo_button.grid(row=2, column=0, columnspan=6)
        self.add_edu_button.grid(row=3, column=0)
        self.add_job_button.grid(row=3, column=1)
        self.add_skill_button.grid(row=3, column=2)
        self.add_cert_button.grid(row=3, column=3)
        self.add_link_button.grid(row=3, column=4)
        self.add_interest_button.grid(row=3, column=5)
        self.save_button.grid(row=4, column=0, columnspan=6)

        # Data Storage
        self.education = []
        self.jobs = []
        self.skills = []
        self.certificates = []
        self.links = []
        self.interests = []
        self.photo_path = None

    def upload_photo(self):
        self.photo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.photo_path:
            print(f"Photo uploaded: {self.photo_path}")

    def add_education(self):
        popup = tk.Toplevel(self.master)
        popup.title("Add Education")
        ttk.Label(popup, text="Institution:").grid(row=0, column=0)
        institution_entry = ttk.Entry(popup)
        institution_entry.grid(row=0, column=1)
        ttk.Label(popup, text="Degree:").grid(row=1, column=0)
        degree_entry = ttk.Entry(popup)
        degree_entry.grid(row=1, column=1)
        ttk.Label(popup, text="Duration:").grid(row=2, column=0)
        duration_entry = ttk.Entry(popup)
        duration_entry.grid(row=2, column=1)

        def save_education():
            institution = institution_entry.get()
            degree = degree_entry.get()
            duration = duration_entry.get()
            if institution and degree and duration:
                self.education.append((institution, degree, duration))
                popup.destroy()

        ttk.Button(popup, text="Save", command=save_education).grid(row=3, column=1)

    def add_job(self):
        popup = tk.Toplevel(self.master)
        popup.title("Add Job")
        ttk.Label(popup, text="Company:").grid(row=0, column=0)
        company_entry = ttk.Entry(popup)
        company_entry.grid(row=0, column=1)
        ttk.Label(popup, text="Position:").grid(row=1, column=0)
        position_entry = ttk.Entry(popup)
        position_entry.grid(row=1, column=1)
        ttk.Label(popup, text="Duration:").grid(row=2, column=0)
        duration_entry = ttk.Entry(popup)
        duration_entry.grid(row=2, column=1)
        ttk.Label(popup, text="Responsibilities:").grid(row=3, column=0)
        responsibilities_entry = ttk.Entry(popup)
        responsibilities_entry.grid(row=3, column=1)

        def save_job():
            company = company_entry.get()
            position = position_entry.get()
            duration = duration_entry.get()
            responsibilities = responsibilities_entry.get()
            if company and position and duration and responsibilities:
                self.jobs.append((company, position, duration, responsibilities))
                popup.destroy()

        ttk.Button(popup, text="Save", command=save_job).grid(row=4, column=1)

    def add_skill(self):
        skill = simpledialog.askstring("Add Skill", "Enter Skill:")
        if skill:
            self.skills.append(skill)

    def add_certificate(self):
        certificate = simpledialog.askstring("Add Certificate", "Enter Certificate:")
        if certificate:
            self.certificates.append(certificate)

    def add_link(self):
        link = simpledialog.askstring("Add Link", "Enter Link:")
        if link:
            self.links.append(link)

    def add_interest(self):
        interest = simpledialog.askstring("Add Interest", "Enter Interest:")
        if interest:
            self.interests.append(interest)

    def save_resume(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        about = self.about_text.get("1.0", tk.END).strip()
        pdf_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if pdf_filename:
            create_pdf(name, email, phone, about, self.education, self.skills, self.certificates, self.links, self.interests, self.jobs, self.photo_path, pdf_filename)
            print(f"Resume saved as {pdf_filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeBuilderGUI(root)
    root.mainloop()
