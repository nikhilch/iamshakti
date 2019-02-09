function fillTweet() {
    var tweetText = document.getElementById("tweetText").value;
    var tweetButton = document.getElementById("tweetButton");
    var tweetLink = "https://twitter.com/intent/tweet?hashtags=IAMSHAKTI&text="+tweetText;
    tweetButton.setAttribute("href", tweetLink);
}
