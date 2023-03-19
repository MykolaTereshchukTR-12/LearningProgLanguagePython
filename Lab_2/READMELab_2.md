# LearningProgLanguagePython
I used the GitHub client to clone the repository. 
You can also use the command: git clone <HTTPS-link_to_repository>
To commit the files I used the command: git commit -m "Lab_2: 1 commit"
Hash of 1 commit: 8404659be0df08f60c7ff36553d88f801b64a72d


I used the command: git checkout -b "BranchOfLab_2". 
It allowed to create a new branch called "BranchOfLab_2" and immediately switch to it.
However, you can use the command to create a branch (without switching): git branch "NameOfBranch",
and the command to switch to it: git checkout "NameOfBranch".


Changes are not reflected, because the branches are independent of each other. 
We have essentially copied the repository files into two branches 
where we can make certain changes without worrying about our changes being propagated to master.
This is very useful when there is a complex project where tasks and parts are developed by different teams.


There are two types of branch merging work in Git: rewinding and full merging. 
If the new commit is a direct descendant of a previous commit, then Git just moves the HEAD pointer to the newer commit. 
When merging different indirect commits of different branches, Git looks for the shared past commit of those branches, and then uses the new and shared branch commits to create a common commit that will contain all the changes in the newly created branch commits. 
However, there is a great chance of a conflict, which I also had. 
Since I was working with the file READMELab_2.md, Git does not create a new commit. 
However, I specified a reason inside the file that described all the new changes. 
I manually resolved the conflict by merging all the changes and editing the file itself. 
After it Git does not detect a conflict and successfully committed the file READMELab_2.md.