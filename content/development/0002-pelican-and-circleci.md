Title: Auto-publish pelican blog to S3 using CircleCI
date: 2016-11-28 12:00
tags: pelican, circleci, s3
slug: pelican-s3-circleci

While having blog powered by [pelican][] is great (because it's fast), creating new post isn't really fun.
There are more than one step to do it:

1. writing the actual post
2. upload to the server (in this case, S3)

If you're on new machine, it's even more painful:

1. clone the repository
2. install pelican's requirements
3. setup S3 credential
4. write the actual post
5. upload to the server

[CircleCi][circleci] has given free tier [for a while now][circleci-free]. So I figured, since I'm using github
for my blog content, I could use it's free continous integration & delivery service to publish my blog easily.

I found [a blog post][pelican-meet-circleci] that gives instruction to do that, but apparently it doesn't work.
`s3cmd` couldn't get the access key ID and secret access key I set. Since CircleCi has [`awscli` preinstalled][circleci-awscli],
it's better to use that one instead. Pelican [doesn't support awscli yet][pelican-awscli],
so there's some steps need to be done to use that.

1. insert your [AWS S3 access key ID, and secret key ID][circleci-awscli]
2. create circle.yml in your repository:  
    :::yml
    dependencies:
      override:
        - pip install -r requirements.txt
        - echo -e "[default] \naccess_key = $S3CFG_ACCESS_KEY \nsecret_key = $S3CFG_SECRET_KEY \n" > /home/ubuntu/.s3cfg

    test:
      override:
        - echo "test"

    deployment:
      aws:
        branch: master
        commands:
          - make html
          - make s3_upload
          
3. commit and push  

You should be able to see the deployment progress on you CircleCI dashboard.

Now, you don't need to create special environment to install pelican etc, just git and text-editor. You could even use
[github's feature][github-new-file] to create blog post directly inside your browser (I wrote this using that!).

[![new post via github][https://s3-ap-southeast-1.amazonaws.com/s.kriwil.com/www/development/0002-new-post-via-github.png]](https://s3-ap-southeast-1.amazonaws.com/s.kriwil.com/www/development/0002-new-post-via-github.png)

[pelican]: https://github.com/getpelican/pelican
[circleci]: https://circleci.com
[circleci-free]: https://circleci.com/blog/continuous-integration-and-deployment-on-circleci-just-got-better-now-its-free/
[pelican-meet-circleci]: http://www.havingatinker.uk/when-pelican-met-circleci.html
[circleci-awscli]: https://circleci.com/docs/continuous-deployment-with-amazon-s3/
[pelican-awscli]: https://github.com/getpelican/pelican/issues/1626
[github-new-file]: https://help.github.com/articles/creating-new-files/
