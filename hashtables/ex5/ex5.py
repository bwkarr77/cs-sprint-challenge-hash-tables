
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for file in files:
        filename = file.split('/')[-1]
        if filename in cache:
            cache[filename].append(file)
        else:
            cache[filename] = [file]

    for query in queries:
        if query in cache:
            # loop through EACH filename at the cache with query name:
            for each in cache[query]:
                result.append(each)
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
