## Postmortem

[Link to postmortem](https://docs.google.com/document/d/1KO9yHYTWqlu4Mmlo6R_PTTPm0rejwDbdFbZNs98GMe4/edit?usp=sharing)

#### Task 0
Write a postmortem.
Requirements:
- Issue Summary (that is often what executives will read) must contain:
	- duration of the outage with start and end times (including timezone)
	- what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
	- what was the root cause
- Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
	- when was the issue detected
	- how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
	- actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
	- misleading investigation/debugging paths that were taken
	- which team/individuals was the incident escalated to
	- how the incident was resolved
- Root cause and resolution must contain:
	- explain in detail what was causing the issue
	- explain in detail how the issue was fixed
- Corrective and preventative measures must contain:
	- what are the things that can be improved/fixed (broadly speaking)
	- a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
- Be brief and straight to the point, between 400 to 600 words

#### Task 1
Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.