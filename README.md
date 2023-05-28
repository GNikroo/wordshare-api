# Word Share

Word Share is a social media site for authors, writers, creators, artists, and anyone hoping to share their thoughts and ideas. Users are encouraged to provide feedback (upon request), interact with others through posts. Word Share provides a creative space for developing their skills as writers.

## Table of Contents

-   [Testing](#testing)
-   [Deployment](#deployment)

## Testing
### Manual Testing during development

- During the development and deployment stage, I ensured that:
    - Initial launch was successful
    - API endpoints:
        - Checked for expected functionality.
        - Verified the HTTP status codes returned correctly.
        - Verified the different HTTP methods worked as expected.
    - Authentication and authorization:
        - Verified protected endpoints with valid and invalid credentials.
        - Verified permissions
    - Error Handling
        - Tested invalid requests and verified error messages were informative.
    - File uploads
        - Verified functionality of image uploads
        - Ensured images were uploaded to the correct Cloudinary path.
    - Integration
        - Verified the integration with the Word Share react app
        - Ensured data is fetched, updated, and deleted correctly.

## Deployment
* My site was deployed to [Heroku](https://ws-api.herokuapp.com/). After creating a secure environment, I created an app on Heroku.
    * Create new app
    * Attach Heroku Postgres as Database in resources
    * Configured variables by matching keys and values both on heroku and in my secure environment
    * Connected the appropriate repository
* After building the app in my IDE, I made a final deployment.
    * Changed debug to false in settings
    * Navigated to the deploy option in my app on heroku
    * Deployed branch