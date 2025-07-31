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
        <a href="licenses.html">Example Licenses</a>
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
<h1>Civil Software Licenses</h1>
    <p>
    This websites presents a set of licenses referred to as <strong>Civil Software Licenses</strong>. Civil software licenses are characterized by containing the following <strong>Civil Clause</strong>, which prohibits the use of the licensed software in the development or construction of any type of weapon:
      
      <blockquote>
      <strong>Civil Clause v1:</strong> This work is provided under the condition that it and any derivatives may not be used in or built into weapons and may not be sold to or used by entities legally authorized to initiate force against persons. Any derivative work’s license must include this clause and may not conflict with it. This clause applies to all sublicensees.
      </blockquote>
    
     The civil cluase states that software distributed under these licenses may neither be sold to nor utilized by entities or institutions that possess the legal authority to employ weaponry, including, but not limited to, military organizations. The Civil Clause further permits the creation of derivative works through a copyleft mechanism, whereby any such derivative work must be distributed under a license that includes the Civil Clause in its entirety and excludes any provisions that contradict or undermine it. <br><br>
     Licenses that incorporate the Civil Clause and otherwise conform to the criteria established for open source software are herein referred to as <strong>Civil Open Source Licenses</strong>.
    We propose <a href="licenses.html">two instances</a> of such licenses, the Civil-M license, which constitutes a civil adaptation of the MIT License, and the Civil-A license, which constitutes a civil adaptation of the Apache 2.0 license.
     <br><br>
    This website discusses the rationale underlying the development of these licenses, the guiding principles of their design, and a answers a range of <a href="qa.html">related questions</a>, including the mechanisms through which these licenses may be enforced.
    </p>
<p>The content of this website is also available as PDF: </p>
<p>📄 <a href="civil_software_licenses.pdf" target="_blank">Civil Licenses PDF</a></p>

<h2>Motivation</h2>
Software developers who publish software are required to incorporate a license that delineates the permitted uses of the software and specifies the conditions under which such uses are authorized.
<br><br>
Developers who do not intend to monetize their software and instead seek to contribute to the public good typically employ free/open-source software licenses.
Such licenses generally impose no restrictions on usage, typically requiring only attribution as a condition of use.
In certain instances, these licenses employ copyleft provisions to ensure that derivative works confer the same rights to users as those granted by the original work.
<br><br>
Where a software developer seeks to restrict certain lawful uses of their software, these licenses are inappropriate as they expressly prohibit such restrictions by their definition.
<br><br>
This website examines the specific circumstance wherein a software developer wishes to restrict the dual-use of their software or other applications that utilize the software to inflict lawful physical violence upon other persons.
<br><br>
Currently, no suitable standardized licenses exist for developers' use, requiring them either to draft custom licenses, which creates legal overhead for themselves and others, or to permit dual-use through open source licenses despite their intention to prevent such applications.
<br><br>
We propose a set of licenses designated Civil Software Licenses to address this problem.
We define a software license as a Civil Software License if it incorporates the Civil Clause above within the license terms and contains no conflicting provisions.

<h2>Autonomous Weapons</h2>
Modern software, particularly software utilizing artificial intelligence, has the potential to render weapons fully autonomous, capable of lethal action without human oversight.
Such weapons are ethically questionable and have the potential to become an existential threat to humanity in the long term.
There is growing concern about such autonomous lethal systems and several <a href="https://www.stopkillerrobots.org/news/2024-nobel-laureate-in-physics-raises-concerns-about-killer-robots/">political efforts</a> to halt or impede their development.
Civil software licenses may contribute to these efforts by rendering open software unavailable for weapon construction, thereby increasing costs and consequently impeding the development of autonomous lethal systems.
"""
    },
    "licenses.html": {
        "title": "Example Licenses",
        "content": """
<h1>Example Licenses</h1>
<p>We designate software whose license incorporates the civil clause and, with the exception of the civil clause, conforms to the conventional <a href="https://opensource.org/osd">open source definition</a> as "civil open source."
The following constitutes two examples of civil open source licenses.</p>
<p>If there are further licenses that you would like us to add to the list please contact us.</p>
<div class="faq">
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Civil-M License</button>
        <div class="faq-answer" hidden>This represents a civil adaptation of the Expat License (commonly known as the MIT license).
It should be noted that our software license is neither endorsed by nor affiliated with the MIT institution.
The objective of this license is to achieve maximum brevity, thereby enabling software developers to rapidly comprehend the requirements applicable to a software repository:
<br><br>
<hr>
Copyright &lt;YEAR&gt; &lt;COPYRIGHT HOLDER&gt;
<br><br>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 
<br><br>
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
<br><br>
Civil Clause v1: This work is provided under the condition that it and any derivatives may not be used in or built into weapons and may not be sold to or used by entities legally authorized to initiate force against persons. Any derivative work’s license must include this clause and may not conflict with it. This clause applies to all sublicensees.
<br><br>
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
<hr>
        </div>
    </div>
    <div class="faq-item">
        <button class="faq-question" aria-expanded="false">Civil-A License</button>
        <div class="faq-answer" hidden> This is a Civil version of the Apache 2.0 license.
Compared to the Civil-M license, it is more comprehensive in its description and contains protection against patent issues, so it is recommended for more complex software projects and companies:
<br><br>
<hr>
Copyright [yyyy] [name of copyright owner]
<br><br>
Licensed under the Civil-A License (the "License");
You may not use this file except in compliance with the License.
<br><br>
TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
<br><br>
1. Definitions.
<br><br>
"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 10 of this document.
<br><br>
"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.
<br><br>
"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.
<br><br>
"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.
<br><br>
"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.
<br><br>
"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.
<br><br>
"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).
<br><br>
"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.
<br><br>
"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."
<br><br>
"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.
<br><br>
2. Grant of Copyright License. Subject to the terms and conditions of this License including the Civil Clause below, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.
<br><br>
3. Grant of Patent License. Subject to the terms and conditions of this License including the Civil Clause below, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.
<br><br>
4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:
<br><br>
    You must give any other recipients of the Work or Derivative Works a copy of this License; and
    You must cause any modified files to carry prominent notices stating that You changed the files; and
    You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and
    If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License.
<br><br>
You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.
<br><br>
5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.
<br><br>
6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.
<br><br>
7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.
<br><br>
8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.
<br><br>
9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.
<br><br>
10. Civil Clause v1: This work is provided under the condition that it and any derivatives may not be used in or built into weapons and may not be sold to or used by entities legally authorized to initiate force against persons. Any derivative work’s license must include this clause and may not conflict with it. This clause applies to all sublicensees.
<br><br>
END OF TERMS AND CONDITIONS
<hr>
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
One of the fundamental principles of free software licenses is that they grant users the freedom to run the program as they wish, <strong>for any purpose</strong>.
This represents a comprehensive conception of freedom that prioritizes the freedom of <strong>the software user</strong>. above all other considerations.
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
        "title": "About",
        "content": """
<h1>About</h1>
<p>Civil Software Licenses were developed by <a href="https://kait0.github.io/">Bernhard Jaeger</a> and <a href="https://www.cvlibs.net/">Andreas Geiger</a>.</p>
<p>If you have feedback please contact us via <a href="mailto:bernhard.jaeger@uni-tuebingen.de">Email</a>.</p>
"""
    }
}

# Write each HTML file
for filename, data in pages.items():
    html = base_template.format(title=data["title"], content=data["content"])
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)

print(f"✅ Static website with centered top menu generated in ./{output_dir}/")
