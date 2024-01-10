# Cloud

## Unpacking the AWS Cloud

> "Amazon has plans to build a new 120-acre data center park in Oregon's Umatilla County, reported The East Oregonian. The facility will join one of three sites in East Oregon. The existing two are located in the Port of Morrow Industrial Park (Boardman) and at the McNary industrial park just outside of Umatilla."

![oregon datacenter](https://raw.githubusercontent.com/tonybutzer/assets/master/et/50-cloud-boardman-oregon-aws.PNG)

### Location Location Location

![region cost graph](https://raw.githubusercontent.com/tonybutzer/assets/master/et/50-cloud-region-cost-variances.PNG)

### AWS Data Centers
![data center guts](https://raw.githubusercontent.com/tonybutzer/assets/master/et/50-cloud-data-center-guts.PNG)

## Cloud Advantages

1. elasticity and quick to scale
2. ephemeral - break it and rebuild 
3. economies of scale
4. many details are now someone else's problems
	- os patching
5. no down time
6. ubiquitous access
7. speed
8. autonomy - never blocked by human or policy

## Cloud Disadvantages

1. must trust the provider
2. when the meter is running - they are billing you
3. costs seem less tangible

## Managing Costs

1. s3 is $.02 per month per gigabyte
2. some instance types are free

` need to write a whole section here`
- point to a notebook and aws cost analyzer
- simple mitigation strategies
	- reserved instances?
	- spot instances
- cloudchecker - is that what ist called - gov and contractor - have and have nots

## Cattle versus Pets

- all compute servers and docker containers are disposable at a moments notice
- this is actually a really good thing
- decouple compute from code
- everything lives in the cloud
- everything can be instantly recreated from a github repo TEXT file
	- i think that is really cool!!!!!

### Pets Service Model

In the pets service model, each pet server is given a loving names like zeus, ares, hades, poseidon, and athena. They are “unique, lovingly hand-raised, and cared for, and when they get sick, you nurse them back to health”. You scale these up by making them bigger, and when they are unavailable, everyone notices.

Examples of pet servers include mainframes, solitary servers, load balancers and firewalls, database systems, and so on.

### Cattle Service Model

In the cattle service model, the servers are given identification numbers like web01, web02, web03, web04, and web05, much the same way cattle are given numbers tagged to their ear. Each server is “almost identical to each other” and “when one gets sick, you replace it with another one”. You scale these by creating more of them, and when one is unavailable, no one notices.

- from --> https://joachim8675309.medium.com/devops-concepts-pets-vs-cattle-2380b5aab313


## Bucket Permissions

### Cross Account

```
{
  "Version": "2012-10-17",
  "Id": "Policy1563360701540",
  "Statement": [
    {
      "Sid": "ListFrom-usgs-CHS-aws",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::574826924367:root"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::ga-et-data"
    },
    {
      "Sid": "GetFrom-usgs-CHS-aws",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::574826924367:root"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::ga-et-data/*"
    }
  ]
}
```
