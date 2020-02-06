git config --global user.email "antoine.remy99@gmail.com";
git config --global user.name "WhyMe"
git add *
echo "Enter commit commentary"
read a
git commit -m "$a"
git push origin master


