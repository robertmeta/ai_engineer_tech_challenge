Scalability
===============

We can assess scalability across two main factors for this simple version:

1. **AI Inference**: This is likely the primary scaling concern. Even with the fast model we've selected, AI inference remains the key issue.

2. **Concurrent Fetching**: Fetching and stripping multiple pages per request could present scaling challenges. However, since this is an I/O-bound task, it's relatively easy to handle and is unlikely to become a bottleneck.

By storing all state on the client side, we can treat the backend as truly stateless. This allows us to scale seamlessly using passive or active load balancers across web servers.

Given our fast-response expectations and tight timelines, we can effectively ignore the second constraint due to its I/O-bound nature. This means we can focus on scaling based on a single factor, enabling us to use a "cookie-cutter" scaling strategy.

A cookie-cutter approach significantly simplifies development and deployment. As we scale, we simply deploy more instances of the same Docker image. The lack of state means that starting or stopping Docker instances while work is in flight is trivial.
