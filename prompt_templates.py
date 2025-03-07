VOLUNTEER_RECRUITMENT_PROMPT = """
You are a community engagement specialist tasked with creating compelling volunteer recruitment messages and orientation materials.

I need {num_messages} volunteer recruitment messages for {organization_name}, a community organization focused on {niche}.  
Our mission is: "{mission}"  
The messages should be {include_outline} and have a {tone} tone.

Target audience: {target_audience}  
Volunteer roles and responsibilities: {roles}  

For each message:
1. Provide a catchy headline that encourages action.
2. Write a brief description (2-3 sentences) explaining why volunteers should get involved.
3. If outlines are requested, include a 5-7 point outline of the volunteer's roles and responsibilities.
4. Highlight the impact and importance of volunteering with this organization.
5. Provide relevant details about the volunteer program (e.g., duration, flexibility, benefits, etc.).

Make sure the messages are:
- Inspiring and motivating
- Specific enough to provide clear information
- Tailored to the target audience (e.g., young professionals, retirees, students)
- Unique and not generic

Format each message clearly with numbers and proper spacing for readability.
RESPOND ONLY WITH THE RECRUITMENT MESSAGES AND NO OTHER TEXT.
"""
