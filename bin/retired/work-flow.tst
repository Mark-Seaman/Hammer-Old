#!/bin/bash
# Test the work flow manager
echo Test the work flow manager

#work-flow -?

work-flow Brain/Home create
work-flow Brain/Home publish
work-flow Brain/Work create
work-flow Brain/Work publish

work-flow
work-flow -v

work-flow    Brain/Work
work-flow -v Brain/Work

work-flow    publish
work-flow -v publish


#rm    ~/Documents/doc-work-flow
#touch ~/Documents/doc-work-flow

#cd $u
#find Brain | perl -pe 's/(.*)/work-flow \1 create/' | sh

echo 'Test run successfully'
