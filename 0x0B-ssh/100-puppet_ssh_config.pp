#!/usr/bin/env bash

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "#!/bin/bash\n\n# Create SSH client configuration file\n\
cat << EOF > ~/.ssh/config\n\
Host your_server\n\
    HostName your_server_ip\n\
    User ubuntu\n\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no\n\
EOF\n",
}
