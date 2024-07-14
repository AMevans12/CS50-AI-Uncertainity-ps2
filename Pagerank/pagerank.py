import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r'<a\s+(?:[^>]*?)href="([^\"]*)"', contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = {p: (1 - damping_factor) / len(corpus) for p in corpus}

    linked_pages = corpus[page]
    if linked_pages:
        for p in linked_pages:
            probability_distribution[p] += damping_factor / len(linked_pages)
    else:
        for p in corpus:
            probability_distribution[p] += damping_factor / len(corpus)

    return probability_distribution

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    visit_count = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))
    for _ in range(n):
        transition_prob = transition_model(corpus, current_page, damping_factor)
        next_page = random.choices(list(transition_prob.keys()), weights=transition_prob.values(), k=1)[0]
        visit_count[next_page] += 1
        current_page = next_page
    
    PageRank = {page: count / n for page, count in visit_count.items()}
    return PageRank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)
    PageRank = {page: 1 / N for page in corpus}
    threshold = 0.001
    while True:
        new_rank = {}
        for page in corpus:
            base_rank = (1 - damping_factor) / N
            contributions = 0
            for q in corpus:
                if page in corpus[q]:
                    outgoing_q = len(corpus[q]) if corpus[q] else N
                    contributions += PageRank[q] / outgoing_q
            new_rank[page] = base_rank + damping_factor * contributions
        
        total_change = sum(abs(new_rank[page] - PageRank[page]) for page in corpus)
        
        # Update PageRank values
        PageRank = new_rank
        
        # Check for convergence
        if total_change < threshold:
            break
    
    return PageRank

if __name__ == "__main__":
    main()
