# Meeting Notetaker Role

Thank you for taking notes for a session! The following are the steps you will follow.

Reminder that we follow the consortium-wide agreed meeting policies. Please refer to them in the [Meeting policies section of the README](../README.md#meeting-policies).

## Take meeting notes live in a Google Docs document

Start with the right meeting notes template:

* [Full consortium meeting notes template](full-consortium-meeting-notes-template.md)
* [Subcommittee meeting notes template](subcommittee-meeting-notes-template.md)

During the meeting you'll take meeting minutes of participants' discussion in a Google Docs document that will be shared as the meeting begins.

You'll add yourself as Notetaker for the meeting in the Google Doc.

### Try to annotate live sections that are [info], [decision], and [todo]

We use an annotation system to note those sections which are [info], [decision], or [todo] so that the meeting minutes can be easily searched.

So in the meeting notes try to annotate live those points which come up that could fall into one of those categories.

Feel free to speak up during the meeting to clarify if something has risen to the level of a [decision] or [todo] if unclear.

## Submit the meeting minutes to the repo

Following the meeting you will select all the contents of the Google Doc, right click, and then click `Copy as Markdown` on the menu that pops up. You have to make sure Markdown is enabled for the document. Enabling it can be done by navigating to **Tools > Preferences** and checking **Enable Markdown**.

Fork this repository if not done yet.

Create a new branch on your fork, navigate to the `minutes.md` for the meeting you've taken minutes for and paste the contents.

### Inserting annotation key

Below the title of the meeting, date and time insert the following annotation key:

```
| Search Key  | Description          |
|-------------|----------------------|
| [todo]      | Action Item          |
| [decision]  | Something decided on |
| [important] | Key information      |
```

(Do not place in a code block in `minutes.md`, but placed in one here to make copying easier)

Open up a pull request from your feature branch into the main repo.

## Monitor till merged

Monitor for any reviews that come through for suggestions on changes and respond back and/or update as necessary.

## You're done!

Thanks again for taking on the notetaker role for the meeting.

