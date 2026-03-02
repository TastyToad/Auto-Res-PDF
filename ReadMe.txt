This costs roughly 10 cents each time it is run , 



The purpose of this project is to automate resume tailoring due to time constraints that come with manually tailoring resumes. 
it takes on average around 30 minutes to tailor a resume manually using Adobe/Word/and even AI prompting. This time can increase exponentially with visually appealing formatas  
This makes it nearly impossible to tailor resumes manually in an efficeinet way.  
The majority of (large) compaies are now utilizing AI services to help with applcicant screening often buiilt into the already bad ATS sytems.
This futher unnesseserally filters out qualified candidates.
having a visually appealing resume is not efficient in the current market and despite the leaps in technological advancements, systems like Workday (yes , stil 0/10 experince for as long as its existed )  can not autofill a phone number correctly from -
normal formats, let alone one thats visually appealing.   
this project creates simplified resume formats that are ATS friedly and easily scanned visually




-> Using a Master Resume in json format,

-> A "Tailored" Resume template in html for simple editing,

-> Python populates the html template using jinja2

->visal html then saved in pdf format 
	-> using very generic format , im willing to bet 90% of automated resumes will look the same so keep that in mind, you should keep a more polished master pdf reserved for real humans


And claudes sonnet 4.5. 













IT IS RECOMENDED to remove company cultre information from used job descriptions
this can lower costs by up to 60% depending on how much spam is includedd 




 PER ClAUDE:
   - Haiku for bulk applications (tech screens)
   - Sonnet for most applications (recommended)
   - Opus only for dream jobs/executive roles\







   

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume</title> 
</head>
<body>
    <header>
        <h1>{{name}}</h1>
        <div class="contact-info">
            {{email}} • {{phone}} • {{city}}","{{state}} • <a href="#">LinkedIn: {{profile}}</a> • <a href="#">{{website}}</a>
        </div>
    </header>

    <section>
        <h2>Professional Summary</h2>
        <p class="summary">
            [Write your professional summary here - 2-3 sentences highlighting your expertise, experience, and key strengths]
        </p>
    </section>

    <section>
        <h2>Professional Experience</h2>
        
        <div class="job">
            <div class="job-header">
                <div class="job-title">[Job Title]</div>
                <div class="date">[Start Date] - [End Date]</div>
            </div>
            <div class="company">[Company Name], [City, State]</div>
            <ul>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
            </ul>
        </div>

        <div class="job">
            <div class="job-header">
                <div class="job-title">[Job Title]</div>
                <div class="date">[Start Date] - [End Date]</div>
            </div>
            <div class="company">[Company Name], [City, State]</div>
            <ul>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
            </ul>
        </div>

        <div class="job">
            <div class="job-header">
                <div class="job-title">[Job Title]</div>
                <div class="date">[Start Date] - [End Date]</div>
            </div>
            <div class="company">[Company Name], [City, State]</div>
            <ul>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
                <li>[Achievement or responsibility]</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Education</h2>
        <div class="education-item">
            <div class="job-header">
                <div class="job-title">[Degree] in [Field of Study]</div>
                <div class="date">[Start Year] - [End Year]</div>
            </div>
            <div class="company">[University Name], [City, State]</div>
            <p>GPA: [X.X/4.0] • Relevant Coursework: [Course 1], [Course 2], [Course 3]</p>
        </div>
    </section>

    <section>
        <h2>Skills</h2>
        <div class="skills-section">
            <div class="skill-item">
                <span class="skill-category">[Skill Category]:</span> [skill], [skill], [skill]
            </div>
            <div class="skill-item">
                <span class="skill-category">[Skill Category]:</span> [skill], [skill], [skill]
            </div>
            <div class="skill-item">
                <span class="skill-category">[Skill Category]:</span> [skill], [skill], [skill]
            </div>
            <div class="skill-item">
                <span class="skill-category">[Skill Category]:</span> [skill], [skill], [skill]
            </div>
            <div class="skill-item">
                <span class="skill-category">[Skill Category]:</span> [skill], [skill], [skill]
            </div>
        </div>
    </section>

    <section>
        <h2>Certifications</h2>
        <ul class="certifications">
            <li>[Certification Name] ([Year])</li>
        </ul>
    </section>
</body>
</html>










<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 850px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 2px solid #333;
            padding-bottom: 20px;
        }
        
        h1 {
            font-size: 32px;
            margin-bottom: 10px;
        }
        
        .contact-info {
            font-size: 14px;
            color: #555;
        }
        
        .contact-info a {
            color: #555;
            text-decoration: none;
        }
        
        section {
            margin-bottom: 30px;
        }
        
        h2 {
            font-size: 20px;
            text-transform: uppercase;
            border-bottom: 1px solid #333;
            padding-bottom: 5px;
            margin-bottom: 15px;
            letter-spacing: 1px;
        }
        
        .summary {
            text-align: justify;
        }
        
        .job, .education-item {
            margin-bottom: 20px;
        }
        
        .job-header, .education-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 5px;
        }
        
        .job-title {
            font-weight: bold;
            font-size: 16px;
        }
        
        .company {
            font-style: italic;
            margin-bottom: 10px;
        }
        
        .date {
            color: #666;
            font-size: 14px;
        }
        
        ul {
            margin-left: 20px;
            margin-top: 10px;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        .skills-section {
            display: grid;
            grid-template-columns: 1fr;
            gap: 10px;
        }
        
        .skill-item {
            margin-bottom: 8px;
        }
        
        .skill-category {
            font-weight: bold;
        }
        
        .certifications li {
            list-style-type: none;
            margin-left: 0;
        }
        
        .certifications li:before {
            content: "• ";
            font-weight: bold;
        }

    </style>

