import os

# Output directory for the static website
output_dir = ""

# Base HTML template with centered top menu
base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }}
        nav {{
            background-color: #2c3e50;
            padding: 1em 0;
            text-align: center;
        }}
        nav a {{
            display: inline-block;
            margin: 0 20px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1em;
        }}
        nav a:hover {{
            text-decoration: underline;
        }}
        .container {{
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border-radius: 6px;
        }}
        h1 {{
            color: #2c3e50;
        }}
        ul {{
            padding-left: 20px;
        }}
        ul li {{
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="qa.html">Q&A</a>
        <a href="about.html">About</a>
    </nav>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

# Page definitions
pages = {
    "index.html": {
        "title": "Civil Software Licenses",
        "content": """
<h1>Welcome to Civil Software Licenses</h1>
<p>This project aims to catalog and analyze software licenses relevant to civil and government software systems. Our goal is to provide clarity, accessibility, and compliance tools to legal and development teams.</p>
<p><a href="civil_software_licenses.pdf" target="_blank">📄 Download Civil Licenses PDF</a></p>
"""
    },
    "qa.html": {
        "title": "Q&A - Civil Software Licenses",
        "content": """
        <h1>Questions & Answers</h1>
        This section addresses various inquiries regarding civil software licenses. Military applications are
        generally employed as exemplars, though the arguments pertaining to policing, intelligence services,
        or weapons systems are, in most instances, analogous. It should be noted that we are not licensed
        attorneys, and this section does not constitute professional legal advice. <br><br>
        If you have further questions that are not yet answered here, please contact us. <br><br>
<div class="faq">
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Are civil software licenses enforceable?</button>
        <div class="faq-answer" hidden>A prevalent concern exists that any form of non-military license lacks enforceability.
The basis of this concern lies in the fact that numerous jurisdictions maintain laws that afford state institutions, including military organizations, protection from legal proceedings (or limit remedies to monetary compensation only).
<br><br>
While it is accurate that certain military entities could potentially utilize software under a civil software license, this likely represents an exceptional circumstance.
The concern regarding dual-use typically does not arise from the software's immediate military application capability, but rather from its potential modification or partial reuse for such purposes.
<br><br>
Consequently, the software must be incorporated into, for instance, a weaponized system.
Military organizations typically do not manufacture weaponized systems. Rather, they procure them from commercial entities.
The pertinent consideration is that defense contractors manufacturing weaponized systems do not necessarily enjoy the same legal immunity as military organizations.
Should a defense contractor utilize civil open source licensed software to construct a weapon, it would constitute a license violation and cause the software creator substantial economic harm.
The civil clause deliberately refrains from making value judgments or providing rationale for the imposed restriction.
Users of civil software licenses may elect to release software under such licenses with the intent of licensing the software to defense contractors under alternative terms.
Therefore, a defense contractor violating the civil clause incurs substantial risk of costly litigation.
<br><br>
The specific legal circumstances will likely vary by jurisdiction.
Certain jurisdictions may exist where civil software licenses lack enforceability.
This does not, however, render civil software licenses without effect.
The aforementioned argument addresses bad actors who deliberately violate license terms.
Many individuals act in good faith and will respect the software author's intentions without the threat of litigation.
Civil software licenses provide developers with the means to express such intentions.
<br><br></div>
    </div>
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Why these specific limitations?</button>
        <div class="faq-answer" hidden>The civil clause restricts the incorporation of software into weapons and usage by institutions authorized to deploy them. The most prevalent examples include military, police, and intelligence services, though we employ the formulation "entities legally authorized to initiate force against persons" to encompass all potential institutions possessing such authority.
<br><br>
The underlying philosophy governing these limitations is that the civil clause restricts the utilization of software for legitimate physical violence and the creation of instruments thereof (weapons).
The state, by <a href="https://en.wikipedia.org/wiki/Politics_as_a_Vocation">conventional definition</a>, maintains a monopoly on the legitimate use of physical force. Most such institutions are therefore governmental entities, though the license extends to private security companies as well.
Other governmental institutions lacking such authority—schools or universities, for example, remain free to utilize civil software.
The rationale for excluding entire institutions rather than solely weapons is that software may be employed in systems that are not directly weaponized but provide support to weaponized systems. A surveillance drone equipped with cameras for target identification represents one such example.
By excluding only institutions legally authorized to deploy weapons, we can preclude these use cases without restricting civilian applications. For instance, drones may be utilized for cartographic purposes.
Sales to individuals are not prohibited, including in jurisdictions where individuals may legally possess weapons (though the software may still not be incorporated into weapons), because individuals lack authorization to initiate force against persons.
<br><br>
Many ideologically motivated licenses provide extensive catalogues of undesirable behaviors that the license restricts, such as terrorism.
The civil clause does not enumerate such behaviors because they are typically unlawful regardless.
Terrorism remains illegal irrespective of license provisions.
One objective of the civil clause is to achieve maximum brevity to minimize legal and administrative overhead while maintaining broad appeal among developers.
<br><br></div>
    </div>
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">What are entities legally authorized to initiate force against persons?</button>
        <div class="faq-answer" hidden>The most common entities to which this refers are military, police, and intelligence services. Depending on the jurisdiction, this may also encompass prisons, border enforcement agencies, specialized enforcement units, private security companies, or other institutions authorized to employ force. The language is maintained in generic terms rather than providing a specific enumeration of institutions and entities, because civil software licenses are international instruments, and variations may exist between jurisdictions regarding which institutions are authorized to use force.
        </div>
    </div>
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Why do civil software licenses use a partial copyleft?</button>
        <div class="faq-answer" hidden>To permit derivative works, a partial copyleft is essential.
Otherwise, users could simply create a copy of the software under different licensing terms.
The copyleft provision in Civil Software licenses is kept minimal by requiring only that users preserve the civil clause and nothing further.
This affords users broad discretion to license derivative works under different conditions, subject to the constraint that the license of the derivative work contains the civil clause and does not attempt to circumvent it.
<br><br>
The partial copyleft also facilitates the commercial distribution of derivative works on public marketplaces.
If, for example, a company publishes a derivative work of civil software as an application on a public application store and a military employee purchases it, then the company has not violated the civil clause; the employee has violated it (because the civil clause will be incorporated into the end user license agreement).
This is, naturally, different if the application store were not public but rather a military internal application store.
In such circumstances, the company is selling the application specifically to the military and is therefore violating the civil clause.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Are civil software licenses free software licenses?</button>
        <div class="faq-answer" hidden>
        The most commonly recognized definition of free software is that provided by the <a href="https://www.gnu.org/philosophy/free-sw.html">Free Software Foundation</a>. The philosophy underlying this concept seeks to maximize the freedoms of software users.
One of the fundamental principles of free software licenses is that they grant users the freedom to run the program as they wish, \textbf{for any purpose}.
This represents a comprehensive conception of freedom that prioritizes the freedom of \textbf{the software user} above all other considerations.
Civil software licenses restrict users from constructing weapons with the software, and as such, do not qualify as free licenses under the Free Software Foundation's definition.
Civil software licenses protect, to some extent, the freedom of individuals upon whom the software is used, given that one purpose of weapons is to curtail the freedom (or life) of those against whom the weapon is deployed.
A design philosophy underlying civil software is also to minimize the restrictions imposed by the license to the absolute minimum, thereby respecting the user's time and freedoms.
<br><br>
In an era where software permeates all aspects of society, we believe it is essential to consider perspectives beyond the software user and to contemplate the broader societal impact that software licenses may have.
We fundamentally support the principle of freedom, while adopting a less absolute position regarding its application.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Are civil software licenses open-source software licenses?</button>
        <div class="faq-answer" hidden>
        The most commonly recognized definition of open source software is that provided by the <a href="https://opensource.org/osd">Open Source Initiative (OSI)</a>, which is a public benefit corporation.
The principles underlying open source software are similar to those of free software, but are more pragmatically oriented, seeking to maximize the convenience of the software user.
The Open Source Initiative's definition does not permit licenses to restrict any party from utilizing the program in a specific field of endeavor.
Civil software licenses likely do not qualify as open source under this definition, as they effectively preclude the defense industry and certain institutions from using the software.
We have introduced the term "civil open source" to clarify this distinction.
<br><br>
The Open Source Initiative addresses in their frequently asked questions the topic of open source software usage by <a href="https://opensource.org/faq#evil">malicious actors</a>:
<br><br>
<blockquote>
Can I stop “evil people” from using my program?

No. The Open Source Definition specifies that Open Source licenses may not 
discriminate against persons or groups. Giving everyone freedom means giving 
evil people freedom, too.
</blockquote>
<br><br>
We wish to identify three deficiencies in this reasoning.
The first issue concerns how the question is framed. It is overly simplistic to categorize individuals as good or evil. It is more appropriate, in our view, to characterize actions as evil, as individuals are often multifaceted.
Therefore, let us rephrase the question to: "Does the license prevent individuals from using my program for evil actions?"
<br><br>
The second point we wish to make is that answering the (modified) question in the negative is unreasonable.
Restricting evil actions does not practically constrain freedom, as any decent individual would not wish to engage in such actions regardless.
The practical difficulty is, naturally, that incorporating language such as <a href="https://www.json.org/license.html">"The Software shall be used for Good, not Evil."</a> into a software license creates legal uncertainty and unnecessary <a href="https://wonko.com/post/jsmin-isnt-welcome-on-google-code/">administrative burden</a> for most software users due to the ambiguity of the term "evil". 
More practical would be to provide a specific enumeration of concrete prohibited applications.
Some licenses employ this approach, but it often wastes the time of license readers.
This is because most evil acts are unlawful regardless of software license provisions.
Civil software licenses do not explicitly prohibit actions such as terrorism because terrorism is unlawful regardless, and we wish to respect the time of license readers.
<br><br>
To conclude, the third deficiency in the OSI argument is that it is incorrect. One can, in most cases, prevent "evil people" from using a program because evil conduct is typically unlawful, and software licenses cannot supersede legal requirements.
<br><br>
Civil software licenses prevent certain forms of evil by restricting the construction of weapons, which can facilitate numerous evil acts.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Is Civil software compatible with the GPL?</button>
        <div class="faq-answer" hidden>
        The GNU Public License v3 contains a provision that invalidates additional restrictions added to the license and incorporates a strong copyleft mechanism.
As such, GPL-licensed software is not compatible with Civil Software because this provision conflicts with the civil clause.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Can my civil open source-licensed repository contain MIT-licensed code?</button>
        <div class="faq-answer" hidden>
        Yes, the MIT license does not contain a copyleft provision.
However, if the incorporated code constitutes a substantial portion, the MIT license requires inclusion of the MIT license in your repository (for example, in the copied file) to indicate that the copied code is MIT-licensed. The civil clause protects your original contributions and derivative works thereof, but not the MIT-licensed software you incorporated.
The same principle applies analogously to similar licenses such as Apache 2.0.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Can I use civil software in military-funded research?</button>
        <div class="faq-answer" hidden>
        In certain jurisdictions, fundamental research at universities is often funded by military or military institutions.
Civil software restricts permissible uses of the code, but does not restrict funding sources.
For example, conducting research on general object detection at a university funded by the military would be permissible.
However, you should be aware that the resulting software from your research cannot be utilized by the military funding agency, due to the copyleft provision in the civil clause.
Another example would be research on drone combat.
This would not be permitted, because you are specifically developing a weaponized system (one component of the development process is the research).
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">What about special case X?</button>
        <div class="faq-answer" hidden>
        In instances where you have a special case and are uncertain whether the license permits it, we recommend consulting the author(s) of the civil software. No plaintiff, no lawsuit.
If you believe you have a special case that is of broader interest, please contact us so that we can incorporate a discussion into this document.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Does the Civil Clause apply to large language models trained on civil software?</button>
        <div class="faq-answer" hidden>
        The Civil Clause applies to all derivative works of the software.
Whether large language models (LLMs) constitute a derivative work of the software upon which they have been trained is an unresolved legal question at the time of writing.
We therefore cannot provide a definitive answer.
We recommend presuming that the answer is affirmative and incorporating the civil clause into the license of LLMs trained on civil software.
This section will be updated should a consensus emerge in the courts.
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">How is a weapon defined?</button>
        <div class="faq-answer" hidden>
        In most cases, the distinction between what constitutes a weapon and what does not is readily apparent. In cases of ambiguity, we refer to the question about special cases. 
        </div>
    </div>
    
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">What if another department at my company produces weapons?</button>
        <div class="faq-answer" hidden>
        There are large corporations today that manufacture a variety of products, ranging from smartphones to warships. Since the civil clause only prevents incorporation of the software into weapons, it is permissible to incorporate the software into smartphones even if another department within the company manufactures warships. Note, however, that the smartphone cannot subsequently be incorporated into the warship, due to the partial copyleft provision.
        </div>
    </div>
</div>

<script>
    document.querySelectorAll(".faq-question").forEach(button => {
        button.addEventListener("click", () => {
            const answer = button.nextElementSibling;
            const isOpen = button.getAttribute("aria-expanded") === "true";

            button.setAttribute("aria-expanded", !isOpen);
            answer.hidden = isOpen;
        });
    });
</script>

<style>
    .faq-item {
        margin-bottom: 20px;
    }

    .faq-question {
        background-color: #ffffff;
        color: #2c3e50;
        border: 1px solid #ccc;
        padding: 14px 18px;
        width: 100%;
        text-align: left;
        font-size: 1.05rem;
        font-weight: 600;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }

    .faq-question:hover {
        background-color: #f2f2f2;
        border-color: #1abc9c;
    }

    .faq-question[aria-expanded="true"] {
        border-color: #1abc9c;
        background-color: #f9fdfd;
    }

    .faq-answer {
        margin-top: 10px;
        padding: 12px 18px;
        background-color: #fefefe;
        border-left: 4px solid #1abc9c;
        border-radius: 6px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        font-size: 1rem;
        animation: fadeIn 0.3s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-5px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
"""
    },
    "about.html": {
        "title": "About - Civil Software Licenses",
        "content": """
<h1>About Civil Software Licenses</h1>
<p>This site bridges the gap between legal frameworks and software development for civil systems. Created by a team of researchers and policy experts, it promotes clarity and open access to software licensing knowledge.</p>
"""
    }
}

# Write each HTML file
for filename, data in pages.items():
    html = base_template.format(title=data["title"], content=data["content"])
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)

print(f"✅ Static website with centered top menu generated in ./{output_dir}/")
