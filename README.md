# Introduction

Message-ID-url aims to be an implementation of the "mid" URL scheme
described in RFC 2392.

# Design

In order to find the corresponding message, the application can be
configured to look in multiple sources. The first source should be
the mail store associated to the mail user agent of the user but 
other sources can be external services like gmane, or even
the Message-ID redirector provided by Debian on
http://lists.debian.org/_MID_

A plugin based architecture should allow to add support lots of
MUA and lots of external sources so that the user can pick those
that are relevant to him. In the default configuration, the software
should try to guess what sources to use.

# Notes

For best results, and avoid some useless redirections through a browser,
it is recommended to register the "x-scheme-handler/mid" MIME type in
the "[Default Applications]" section of ~/.config/mimeapps.list and
associate it with "open-msgid.desktop".

```
$ head -n 2 ~/.config/mimeapps.list
[Default Applications]
x-scheme-handler/mid=open-msgid.desktop
```

You can double check that the association is properly recorded with this
command:

```
$ xdg-mime query default x-scheme-handler/mid
open-msgid.desktop
```
