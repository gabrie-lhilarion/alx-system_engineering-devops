Incident Postmortem: Unexpected Page Loading Issue
Issue Summary:
Users of WifoStore are not able to access the website, though the webpage opened, it was just a plank white page
Duration: Start Time: 7:50 PM, Dec 12, 2016, GMT+1; End Time: 12:50 PM, Dec 14, 2016, 
Impact: Users experienced an unexpected issue where the home page failed to load. Approximately 100 percent of users were affected.
Root Cause:
The root cause of the issue was identified by me as a "headers already sent" error due to whitespaces and newline characters between the <?php opening tag and the session_start() function. 
.
Timeline:
7:50 PM, Dec 12, 2016: Users reported unexpected page loading issues.
8:00 PM, Dec 12, 2016: Initial investigation started by me.
Noon, Dec 14, 2016: I discovered that the issue was caused by whitespace or newline characters between the  <?php opening tag and the session_start() function.
12:50 PM, Dec 14, 2016: I fixed the issue in two ways:  removing the whitespaces,  and newlines and adding the ab_start() function. Any of the two salved the case. But I used both.
.
Misleading Investigation Paths:
Initially, the team suspected database connectivity issues or server configuration problems, leading to efforts in those areas before identifying the cause. 




Resolution:
The immediate resolution involved adding ab_start() at the beginning of the affected PHP files to start output buffering and prevent any unintentional output.
Corrective and Preventative Measures:
Conduct a thorough review of all PHP files in the application to identify and remove any whitespace or newline characters before the session_start() opening tag.
Implement linting or code formatting tools in the development workflow to catch such issues early during code reviews.
Action Items:
I conducted a code review of the PHP file to identify and remove whitespace or newline characters before the session_start().
Integrate linting or code formatting tools into the development workflow to prevent similar issues in the future.
Conclusion:
The unexpected page loading issue, caused by a "headers already sent" error due to whitespaces and newline characters before session_start() resulted in user disruption. By promptly identifying and implementing a temporary fix, followed by corrective measures to prevent recurrence, we have improved the reliability and stability of our application.