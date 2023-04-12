contents = ["All men should fight", "All workers should work hard", "All women should look good"]
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for content, filename in zip(contents,filenames):
    file = open(f'{filename}','w')
    file.writelines(content)