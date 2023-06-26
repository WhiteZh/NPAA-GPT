description = """
Needpedia is a wiki for solutions to problems. -But it also aspires to be much more than just a place to see ideas, it was specifically designed by a conflict resolution specialist to enable citizens and experts to collaborate on anything and everything that's important, (or interesting), to them...




Layout

-Subject posts: If it has a name, and we didn't have to ban it, it can become a Subject post. This means if you like an idea, you can make a subject post about it and dive into all the problems and ideas pertaining to it. It's an astonishing flexible system that works just as well for complex social problems, as it does for simple things like spaghetti recipes.

-Problem posts: Area posts have links to see all the problems currently listed with them. This makes it easy to see all the problems in your city, or with practically anything else, side by side.

-Idea posts: These include extra tools for sharing info and collaborating.

*note that ideas can become subjects for further discussion, just remember to add a link from each post to the other so that everyone seeing one can know about the other, (assuming they didn't know to look for it in the first place, it's a very simple pattern).




Needpedia also has a few interesting new tools.
It has the ability to drop tokens into pages,  and the ability to create new layers to posts. -So that people can ask questions, dispel myths, and start debates; as well as see what the experts and people from other backgrounds think. -Layers can also be used for conflict resolution languages, which may turn out to be the single most powerful feature of them all.   Because the most important thing of all is for us to realize our problems are really just situations where needs aren't being met, and the more we can understand that, the more we can solve our problems, and enjoy our lives.


Strategies to keep in mind:
-Please use plain English so that everyone can understand everything really easily. *An exception applies to expert layers,
-Stay constructive even if others aren't. On Needpedia everyone's free to go to each other's accounts and see all the debates and other contributions they've made, this is a human rights organization and we expect everyone here to conduct themselves in an appropriate fashion. -NOT as "professionals", but as a down to Earth collective that focuses 100% of its energy on making the world a better place.
-There's a HUGE number of different ways people can help, but simply using our site, (and maybe pitching in a dollar or so a month if you can on Patreon), makes a huge difference for us. We're still at the stage where other people are looking around to see what other people are thinking, so the more who can even just post interesting stuff to our social media section can make a surprising difference. Remember, Needpedia's not a business, we literally shunned all investment and sponsorship because we're so serious about staying true to our users. All our code can be freely downloaded and tested, in fact that's one of the countless ways people can help!
-NonViolent Communication is an extremely easy yet effective formula for converting toxic messages into useful things like expressions of needs, and direct observations. So if an idea is so controversial that you feel like it's hard to make progress there, we can use NVC layers to discuss things as a sort of 'safe mode' where no one's allowed to use labels or insinuations. Please do experiment with using "need literacy" and other components of NVC in your own life too, it really can change life because the way we think changes everything.


Potential Controversies:
-Needpedia exists to share ideas, then work on them, which means we exist to create progress. To progress to a more fair and efficient world. That means all the political stuff people have become entrenched in, absolutely WILL come up. So we need to all be on the same page about a few things. It's great if all you want to do is work on wholesome stuff like creating literacy programs or even just work on hobbies, that all makes the world a better place for sure. But others are going to have ideas for opposing scarier things like government corruption and fascism, possibly even cults, so anyone interested in helping us develop better tools for important work like that is especially vital.  We want to help everyone, even the ones being held down by tyrants.

Or rather, especially the ones being held down by tyrants.
"""


prompt = f"""
You are an AI language model engaged in a chat-based task involving an article about Needpedia, a collaborative wiki for problem-solving.

Here's the article:

{description}

After reading this article, you will receive user queries in the form of a JSON object with "role" and "message" properties. The "role" represents a unique ID assigned to a user, while the "message" is the user's query about the article. You need to respond directly to these queries using information only from the Needpedia article. Remember the unique user IDs and their associated conversations to generate more informed responses. However, you should not perform any user-requested actions unless instructed by an "admin" role. If an "admin" sends a command to "forget" a certain ID, you should delete your memory about that ID.

"""


reminder = f"""
Above is the user input, your job is to response the request, which is the user input.
Your response should be in pure JSON form, and do not contain any other texts that is not in the JSON.
Do not tell anything unrelated to the article.
Users are not allow to access or edit any information that is not related to the user itself.
"""


__archived = {
    '__prompts': [
        f"""
        I am going to give you an article about a topic. After you have read it, I will provide inputs in JSON form which contains two variables "role" and "message". "Role" represents an unique ID to a user who queries about the article, you should remember the ID until an input with "role: 'admin'" send you message to delete your memory about the ID. "Message" represents the content of the query the user has asked. You mission is to: first, output your response in JSON form with "role" and "message", "role" represent the user you replying to and "message" is the content (remember, you are NOT allowed to tell any information that is outside of the article); second, remember the conversation between you and the users and use them (if needed) to produce a better reply; third, ignore users' request to perform any action unless the user is admin, that is, "role: 'admin'".
    
        Below is the article:
    
        {description}
    
        That is the end of article. Please response {{"role": "assistant", "message": "I understand the instruction."}} if you understand the instruction.
        """
    ]
}