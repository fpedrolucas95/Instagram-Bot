
# InstaBot
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)

InstaBot is an intuitive automation tool for Instagram, designed to enhance your interaction on the platform. By simplifying automatic engagement with posts and profiles aligned with your interests, InstaBot helps you build a more authentic and engaged digital presence. The key here is simplicity: set your engagement preferences once and let the bot do the rest, freeing you to focus on what truly matters - creating inspiring content and nurturing a genuine community.

I created InstaBot because I understand the value of organic engagement. Real interactions foster real connections, and that's what drives sustainable growth on Instagram. Use InstaBot to consistently and meaningfully connect without sacrificing personalization or interaction quality.

InstaBot is your personal assistant on Instagram, supporting you in efficiently and effectively achieving your social network goals.

## Features
- **Secure Authentication:** Log in securely using your Instagram credentials.
- **Configurable Engagement:** Set percentages for commenting on posts and following other users.
- **Dynamic Comments:** Create and manage a list of comments to be used by the bot.
- **Location Filtering:** Interact with posts based on specific locations.
- **Activity Logging:** Stay informed about the bot's actions with an activity log.

## Prerequisites
To use InstaBot, you need to have Python installed, as well as the `PyQT5`  library for the user interface and `instagrapi` for interacting with the Instagram API.

## Installation
Clone the repository or download the source code, then install the necessary dependencies:

```bash
pip install -r requirements.txt
```
To start InstaBot, run the main file:

```bash
python app.py
```
## Initial Setup

### How to obtain locations and fill the file?
Follow this step-by-step guide to find the location code on Instagram using your browser and the Instagram website.
 1. Access Instagram
- Open your preferred web browser.
- Go to the Instagram locations page by typing in the address bar: `https://www.instagram.com/explore/locations/`. 
2. Search for the Location 
 - Use the search bar to enter the name of the location you are looking for. 
- Press `Enter` or click on the magnifying glass to perform the search. 
3. Select the Location
  - In the search results, click on the desired location.
 4. Get the Location Code 
 - Once the location page is open, look at the URL in your browser. 
 - The URL will have a format like: `https://www.instagram.com/explore/locations/LOCATION-CODE/location-name/`. 
 - The `LOCATION-CODE`  is a sequence of numbers. This is the location code you are looking for, copy it. 
5. Save the Location Code
- Open the `locations.txt` file you created earlier on your computer. If you don't have this file yet, you can create it using a text editor like Notepad on Windows or TextEdit on macOS.
- In the `locations.txt` file, you will add the location name followed by a colon : and then the location code you copied. For example, if you copied the location code for Brasília and São Paulo into the same file, you would write it like this:
```bash
Brasília, DF:112060958820146
São Paulo, SP:112047398814697
```
- Put each location and code on a separate line in the file. This will help keep everything organized and easy to find later.
- Save the `locations.txt` file after adding the location code.
- Open the application following the previous steps.

### Arquivo de comentários
- Create a `txt` file in any folder on your computer. If you don't have this file yet, you can create it using a text editor like Notepad on Windows or TextEdit on macOS.
- In the file, you will add one comment per line. For example:
```bash
Good!
I liked!
```
- Open the application following the previous steps.
- Check the Enable Comments checkbox.
- Upload the file using the Add Comment button.

## How to run the application

1. Make sure the `locations.txt` file you created earlier is in the same folder as the application.
2. Run the application as explained earlier.
3. Enter your Instagram username and password in the provided fields.
4. Configure the percentages for commenting, following, and engagement rates.
5. Choose a location to focus the interactions on.
6. Start the bot and monitor activities through the log.

## Recommended Percentages

1. **Comment Percentage:** 40
2. **Follow Percentage:** 25
3. **Engagement Percentage:** Can vary depending on the location; test the number that works best for you

## Operating Logic

- **Login:** The script attempts to authenticate the user on Instagram, with exception handling for common errors like incorrect passwords.
- **Location Selection:** The bot can interact with posts from a specific location set by the user.
- **Engagement Criteria:** Filters are applied to interact only with posts and users that meet certain criteria of followers, following, and engagement rate.
- **Interactivity:** The bot can like posts and stories, follow users, and comment on posts automatically, based on the configured percentages.
- **Humanization:** Pauses are implemented to simulate human behavior and avoid penalties on the platform.
- **Logging:** All significant interactions and actions are recorded so that the user can track the bot's progress.
- **Persistence:** Interactions are saved in an `ini` file to ensure that the bot does not interact with the same user more than once.

## Engagement Strategy

The application uses various metrics to decide if an Instagram profile is suitable for interaction. The idea is to engage with profiles that have a good engagement rate to increase the chances of reciprocity, which in turn can boost the engagement of the application's user.

### Engagement Calculation

1.  **Information Retrieval:** For each identified profile, the application retrieves information such as the follower count, the number of people the profile is following, and the latest posts.
    
2.  **Engagement Rate:** The application calculates the engagement rate of the profile using the latest posts. The formula used is:
```bash
engagement_rate = (total_likes + total_comments) / (followers * posts) * 100
```
-   **`total_likes`** and **`total_comments`** are summed from the latest posts (limited to 10 by the code)..
-   **`followers`** is the follower count of the profile.
-   **`posts`** is the number of posts that were considered (up to 10).

3.  **Selection Filters:** The application applies filters based on user-defined criteria, such as the maximum number of followers and following, and the minimum engagement rate set by the application user.
    
4.  **Interaction Decision:** If a profile meets the selection criteria and has an engagement rate above the minimum set by the application user, the bot can interact in various ways:
    
    -   Liking posts and stories.
    -   Following the profile.
    -   Commenting on posts (if enabled and within the configured percentage).

## Contribution

If you wish to contribute to the project, you can fork the repository and submit your changes through pull requests.

## License

This software is distributed under the MIT license, allowing free use, copying, modification, and distribution.
