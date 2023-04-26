from flask import Flask, jsonify, request, redirect, url_for, session
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
a="react"


@app.route('/post_data', methods=['POST',"GET"])
def post_data():
    # a="react"
     text = request.json.get('text')
     a=text
     print(a)
     projects_df = pd.read_excel('ASIANPAINT.xlsx')
    #  print(a)
     candidate_skills = "react"
     candidate_skills = candidate_skills.split(',')

    # Create a TF-IDF vectorizer
     tfidf = TfidfVectorizer()

    # Fit the vectorizer on the technology stack column
     tfidf.fit(projects_df['Required_Skills'])

    # Transform the technology stack column
     technology_stack_tfidf = tfidf.transform(projects_df['Required_Skills'])

    # Transform the candidate's skills into a TF-IDF vector
     candidate_skills_tfidf = tfidf.transform([' '.join(candidate_skills)])

    # Calculate the cosine similarity between the candidate's skills and the technology stack
     similarity_scores = cosine_similarity(technology_stack_tfidf, candidate_skills_tfidf)
    # print(similarity_scores)
     score_list=[]
     for i in range(len(similarity_scores)):
         score_list.append(similarity_scores[i][0])
        
        
     sorted_list = sorted(score_list, reverse=True)
    # print(sorted_list)

     indices = [i[0] for i in sorted(enumerate(score_list), key=lambda x:x[1], reverse=True)]




    # print(indices)

     new_list = []
     for i in range(len(sorted_list)):
         if sorted_list[i] != 0:
             if i > 0:
                 new_list.append(indices[i-1])
                
             else:
                 pass
            
    # print(new_list)


    # l=[]
    # for i in range(len(similarity_scores)):
    #     if similarity_scores[i][0]!=0:
    #         l.append(i)
    #     else:
    #         pass
    # print(l)


     t=[]
     u=[]
     v=[]
     d=[]


     for i in range(len(new_list)):
         a=new_list[i]
         recommended_project = projects_df.loc[a, ['Project_domain', 'Project_title','Required_Skills','Difficulty_level']]
         t.append(recommended_project["Project_domain"])
         u.append(recommended_project["Project_title"])
         v.append(recommended_project["Required_Skills"])
         d.append(recommended_project["Difficulty_level"])
         
         

        # v.append(recommended_project["Project_desc"])
    # Print the recommended project
        # print('Recommended Project:')
        # print(f'Objective: {recommended_project["Project_domain"]}')
        # print(f'Output: {recommended_project["Project_title"]}')
        # print(" ")
     print(t)
     print(u)
     data={"project":u, 'age': v,"p_name":t, "diff":d}
    # print(v)
     return jsonify(data)  

    

@app.route('/get_data/<string:name>', methods=['GET','POST'])
def get_data(name):

    #  a = session.get('a')
    #  if not a:
    #     return redirect(url_for('post_data'))

    # projects_df = pd.read_excel('ASIANPAINT.xlsx')
    # candidate_skills = a
    # candidate_skills = candidate_skills.split(',')
    # data = {'project': ['React','ML','Angular','NodeJS','Deep Learning',a], 'age': 30}
    # print(data)
    # return jsonify(data)
     projects_df = pd.read_excel('ASIANPAINT.xlsx')
    #  print(a)
     candidate_skills = {name}
     #candidate_skills = candidate_skills.split(',')

    # Create a TF-IDF vectorizer
     tfidf = TfidfVectorizer()

    # Fit the vectorizer on the technology stack column
     tfidf.fit(projects_df['Required_Skills'])

    # Transform the technology stack column
     technology_stack_tfidf = tfidf.transform(projects_df['Required_Skills'])

    # Transform the candidate's skills into a TF-IDF vector
     candidate_skills_tfidf = tfidf.transform([' '.join(candidate_skills)])

    # Calculate the cosine similarity between the candidate's skills and the technology stack
     similarity_scores = cosine_similarity(technology_stack_tfidf, candidate_skills_tfidf)
    # print(similarity_scores)
     score_list=[]
     for i in range(len(similarity_scores)):
         score_list.append(similarity_scores[i][0])
        
        
     sorted_list = sorted(score_list, reverse=True)
    # print(sorted_list)

     indices = [i[0] for i in sorted(enumerate(score_list), key=lambda x:x[1], reverse=True)]




    # print(indices)

     new_list = []
     for i in range(len(sorted_list)):
         if sorted_list[i] != 0:
             if i > 0:
                 new_list.append(indices[i-1])
                
             else:
                 pass
            
    # print(new_list)


    # l=[]
    # for i in range(len(similarity_scores)):
    #     if similarity_scores[i][0]!=0:
    #         l.append(i)
    #     else:
    #         pass
    # print(l)


     t=[]
     u=[]
     v=[]
     d=[]


     for i in range(len(new_list)):
         a=new_list[i]
         recommended_project = projects_df.loc[a, ['Project_domain', 'Project_title','Required_Skills','Difficulty_level']]
         t.append(recommended_project["Project_domain"])
         u.append(recommended_project["Project_title"])
         v.append(recommended_project["Required_Skills"])
         d.append(recommended_project["Difficulty_level"])
         
         

        # v.append(recommended_project["Project_desc"])
    # Print the recommended project
        # print('Recommended Project:')
        # print(f'Objective: {recommended_project["Project_domain"]}')
        # print(f'Output: {recommended_project["Project_title"]}')
        # print(" ")
     print(t)
     print(u)
     data={"project":u, 'age': v,"p_name":t, "diff":d}
    # print(v)
     return jsonify(data)  

if __name__ == '__main__':
    app.run(debug=True)
