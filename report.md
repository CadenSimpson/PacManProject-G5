Part 1:
Each member worked on a feature and a test for that feature, so Vincent Nguyen fixed items.py and added test_items.py, Kevin Ferry fixed ghost.py and added test_ghost.py, Caden Simpson fixed pacman.py and added test_player.py, Meherzan Gai fixed game_board.py and added test_game_board.py. Caden created a GroupMe so we could communicate, and he forked the repository and shared to the rest of the group. Each member also did a pull request and approved one as well, and we found some bugs but decided to report Caden's.

Part 2:

Caden wrote the report and did step 1, changing the instances of player to pacman (report is included below). 
Vincent worked on part 2, securing the sensitive information.
Meherzan worked on step 3, implementing the actions CI/CD pipeline.
Vincent and Kevin both helped with merging the pull requests and reviewing the changes.


Response for: Step 1) Rename components and implement updates

These were the commands that I used to rename all instances of "player" to "pacman." First was renaming the files, which I just used the git mv command, renaming the previous files to the new versions manually. 

Then for replacing the player keyword inside the files, I wanted a command that would easily accomplish this automatically. For this, I used the sed and grep commands. Grep is used to find all files in the directory that contain "player" so that we update them. Sed was used to find the exact matches in the text of the "player" and to replace it with "pacman". There are two versions of the sed, grep command so that capitalization can be dealt with easily.

From the two above, I did them both inside a newly created branch called player_renamed_pacman, afterward pushing it to git and merging the branch.

Lastly, I had to rename the branch feature/player. To do this, I switched to the branch and used git branch -m to rename the branch. Then I pushed the "new"/renamed branch to github, and deleted the old branch.

There was one small problem in replacing all instances (replacing "player" in the part 2 instructions), which was just a one off case and individually was easy to fix it.

Renaming the files:
git mv player.py pacman.py
git mv test_player.py test_pacman.py

Replacing in the files:
sed -i 's/\<player\>/pacman/g' $(grep -Rl player .)
sed -i 's/\<Player\>/Pacman/g' $(grep -Rl Player .)

Renaming the branch (Inside the branch feature/player):
git branch -m feature/pacman
git push origin feature/pacman
git push origin –delete feature/player
