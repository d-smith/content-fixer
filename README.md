# content-fixer

Update content-type for certain files if they hit the bucket with the wrong content type.

Note that you get two events - one for the initial write to the bucket, and one on update of the content type, which can wind up in an infinite loop if you are not careful.

Note the s3 premissions need to be refined.

Deploy is two steps - sls deploy, sls s3deploy. npm install is needed to pick up the s3 plugin

## Attributions

Cat by Alina Oleynik from the Noun Project
