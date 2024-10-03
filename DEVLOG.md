Devlog
======
This is a log of developers thoughts, newest at the top.


2024-10-03 01:01:26 - Robert Melton
-----------------------------------
Using bing as the backend for search because it is not current constrained and
the setup is better the Google GCE, full web search off one API key.


2024-10-03 00:55:44 - Robert Melton
-----------------------------------
Just got back to working on this, finishing up design and going to use teraform,
linode and a single cookie cutter docker as it likely will scale on a single
point, the LLM performance.


2024-09-30 16:26:34 - Robert Melton
-----------------------------------
Sadly, Ollama on Apple M1 series when in the docker runs painfully slow.

https://chariotsolutions.com/blog/post/apple-silicon-gpus-docker-and-ollama-pick-two/

We can handle this by optionally linking up to the host using the
host.docker.intenral to reference the host and to pass in the ollama host and
port via .env making the docker still work out of the box but also work with the
accellerated version if developer wants.


2024-09-30 12:28:32 - Robert Melton
-----------------------------------
Tested some models out, cohere small, gemma2 small and llama 3.2 tiny (1B, 3B)
and I think the 3B is ideal for this use case due to speed of it and the small
size. Optional accelleration with GPU means easy local dev on all platforms and
optoimized production deploys.


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
