from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.POST.get('fulltext')
    counttext = fulltext.split()
    textdic = {}
    for word in counttext:
        if word in textdic:
            textdic[word] += 1
        else:
            textdic[word] = 1

    sortedword = sorted(textdic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'counttext': len(counttext), 'sortedword': sortedword})
