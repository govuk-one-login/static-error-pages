# Outage Explanation Page

This repository serves a static index.html page that provides an explanation for outages in the GOV.UK OneLogin journey.

In instances where the frontend services are inaccessible or down for any reason, users may encounter a generic Cloudfront error page. To address this, this repository hosts a custom error page to provide users with information about the outage.

### Placeholder Error Pages

Currently, all error pages within the src directory are simply copies of the main index.html page. This means that users see the same generic page regardless of the specific error they encounter. In the future, these error pages will be updated to provide more informative and relevant messages based on the type of error that occurred, enhancing the user experience and helping to troubleshoot issues more effectively.