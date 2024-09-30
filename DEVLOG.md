Devlog
======
This is a log of developers thoughts, newest at the top.


2024-09-30 10:08:21 - Robert Melton
-----------------------------------
Looked at the existing solutions that are in public

- https://github.com/manikbali/ai_engineer_tech_challenge Incomplete.

- https://github.com/Dellrodar/ai_engineer_tech_challenge This one is great,
ollama linked to 3.1, terrific README. EFS for model storage is fine, but why?
Unless fine tuning them.

- https://github.com/rtyildirim/ai_engineer_tech_challenge Ah, CDK, this is sort
of my naive approach would be, I think this is probably in a AWS envirionment
close to the right way, would need to use developer stacks to make the dev
experience at all passible. Would not use that model for this work, it is hugely
expensive.

- https://github.com/Sipty/ai_engineer_tech_challenge Love the rabbitmq and
  clean python backend. This README.md is like a very good DEVLOG.md, I would
  love this in a DEVLOG sort of daily process format. CORS issues as noted are
  incredibly annoying, I literally had a t-shirt made for my team that says "It
  is always CORS", made.


2024-09-30 09:54:53 - Robert Melton
-----------------------------------
I looked at using OCI (Oracle) as the GPU cost is an insanely good value, they
are betwen 4x and 10x chaeper per transaction unit versus AWS. Account has a lot
of friction points, including a human approval of my account!


2024-09-30 09:28:40 - Robert Melton
-----------------------------------
Due to the way github works, having people fork the project will make the forks
public forever, with this is mind, I dug into the 4 public repos and found some
interesting stuff.

- https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks

- Added a note to [FEEDBACK.md](./FEEDBACK.md)
- Added a note to [FRICTION.md](./FRICTION.md)
