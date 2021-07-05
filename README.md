# Webscraper - *SupremeDropBot*

**SupremeDropBot** a webscraper for the SupremeNewYork website. It allows you to fill in your desired item and payment information. Then once the product launches you will be redirected to the captcha at the end of checkout.

By: **Mason Horne**

## Images

Here is the input form for all information needed to complete a transaction:

![](https://i.imgur.com/96eUNp4.png)


## Notes

This project uses the requests library and BeatifulSoup4 to scrape the website. It also uses the Tkinter library for the GUI that collects transaction information.

- [x] Timer to allow for multiple attempts until the product drops (or 15 minute timeout is reached).
- [x] GUI that collects all user information needed by the site.
- [x] Webscraper that handles finding the given item with provided criteria.

## License

    Copyright 2021 Mason Horne

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.


