# Analysis-of-the-uptime-and-downtime-of-a-website-and-comparing-with-Cloud-SLAs-for-Violation
REPORT FOR THE PROJECT

<h2> Attribution </h2>

Hello everyone, you are welcome to make use of this Report and learn from it but please do not copy without giving attribution to the author.

<h2> Abstract </h2>

<p style='text-align: justify;'>In cloud computing, service level agreements (SLAs) are legal agreements between a service provider and consumer that contain a list of obligations and commitments which need to be satisfied by both parties during the transaction. From a service provider's perspective, a violation of such a commitment leads to penalties in terms of money and reputation and thus has to be effectively managed. In the literature, this problem has been studied under the domain of cloud service management. One aspect required to manage cloud services after the formation of SLAs is to predict the future Quality of Service (QoS) of cloud parameters to ascertain if they lead to violations. Various approaches in the literature perform this task using different prediction approaches however none of them study the accuracy of each. However, it is important to do this as the results of each prediction approach vary according to the pattern of the input data and selecting an incorrect choice of a prediction algorithm could lead to service violation and penalties. In this, we test and report the accuracy of time series and machine learning-based prediction approaches. Our analysis helps the cloud service provider to choose an appropriate prediction approach (whether time series or machine learning based) and further to utilize the best method depending on input data patterns to obtain an accurate prediction result and better manage their SLAs to avoid violation penalties.</p>

<h1> Chapter 1 </h1>

<h2> Introduction </h2>

<h3> 1.1 OVERVIEW & MOTIVATION </h3>

Cloud computing is being adapted by a growing number of individuals and enterprises due to its wide range of services, including the elastic scaling of resources, automatic service deployment and virtualized resources with its benefits of being economical and easily manageable in nature. Due to these features, cloud computing has become the first choice for many small to large organizations. Gartner Research states that cloud computing is a rapidly emerging technology on which organizations spent an estimated $677 billion from 2013 to 2016. According to a survey Conducted by an IT decision maker for large companies, more than half of the respondents (68%) expected that 50% of their I.T. resources would be migrated to cloud platform. In cloud computing, service level agreement(SLAs) are legal agreements between a service provider and consumer that contain a list of obligations and commitments which need to be satisfied by both parties during the transaction. Violation of such a commitment leads to penalties in terms of money and reputation and thus has to be effectively managed. An SLA is a legal contract which includes service obligations, deliverability, service objectives and service violation penalties. An SLA is not only used to measure the performance of the provider, it also helps to resolve disputes regarding consumer duties. An SLA comprises one or more objectives, called service level objectives (SLO), which comprise one or many low-level metrics. Violations in SLAs leads to penalties in form of money and loss of reputation and thus it needs to be effectively managed. Our analysis will help to test and report the accuracy of time series based machine learning prediction approaches and help the cloud service provider to choose an appropriate prediction approach and utilize the best method depending on input data patterns.

<h3> 1.2 OBJECTIVE </h3>

We are going to propose a new framework in order to obtain the best method for predicting the QoS based on the input and output pattern, CPU, and memory. This approach ranks the different prediction approaches according to its predicting accuracy, and this determines the SLA violations. Using this method, the service providers select the method since incorrect adoption causes SLA violation and penalties. We will test and report the accuracy of the time series and machine learning based prediction approaches. Our analysis helps the cloud service provider to choose an appropriate prediction approach and further to utilize the best method depending on input data patterns to obtain an accurate prediction result and better manage their SLAs and to avoid violation penalties.

<h3> 1.3 SCOPE </h3>

The project will determine the SLA Violations between Cloud Service Provider and Cloud Consumer and on that basis we will calculate the penalties that cloud service provider will have to pay due to the violation of SLA terms and conditions. For more precise results time series algorithm of Machine Learning will be used to calculate the penalties that service provider will pay for the violation of SLA (Service Level Agreement) terms and conditions. This project can be widely used in IT industry to ensure service availability to consumer with respect to all terms and conditions and it will result in increased productivity.

<h1> Chapter 2 </h1>

<h2> Software Requirements & Analysis </h2>

<h3> 2.1 FEASIBILITY STUDY </h3>

The project is feasible in all aspects as it can be developed easily and is easy to use. We have developed a server and a client which is implemented by using Flask framework. In this project client requests, server responds. Whether server responds or fails to responds, in each case, log file is created displaying whether the server was up or down. So various time series based machine learning algorithm can be applied to log file data to predict SLA violation. On the basis of SLA Violation, Cloud Service Provider will be liable to pay the compensation to its customer.

<h3> 2.2 REQUIREMENT ANALYSIS </h3>

   <h4>2.2.1 System Hardware and Software Specifications Hardware Specifications: </h4>
   
   A PC with following configurations was used for this purpose:
    
   <b> CPU </b>
   1. RAM: 4 GB
    
   2. No of cores:4
    
   3. No of threads:8
    
   4. Clock Speed: 2.13GHz
    
   5. Instruction Set: 64 bit
    
   <b> Software Specifications: </b>
    
   1. Python3.6
    
   2. Flask
    
   3. Panda Library

<h3> 2.3 CLOUD SLAs </h3>

A cloud SLA (cloud service-level agreement) is an agreement between a cloud service provider and a customer that ensures a minimum level of service is maintained. It guarantees levels of reliability, availability and responsiveness to systems and applications, while also specifying who will govern when there is a service interruption. A cloud infrastructure can span geographies, networks and systems that are both physical and virtual. While the exact metrics of a cloud SLA can vary by service provider, the areas covered are uniform: volume and quality of work -- including precision and accuracy -- speed, responsiveness and efficiency. The document aims to establish a mutual understanding of the services, prioritized areas, responsibilities, guarantees and warranties provided by the service provider.
An SLA will commonly use technical definitions that quantify the level of service, such as mean time between failures or mean time to repair, which specifies a target or minimum value for service-level performance. A typical compute and cloud SLA articulates precise levels of service, as well as the recourse or compensation the user is entitled to should the provider fail to deliver the service as described. Another area to consider carefully is service availability, which specifies the maximum amount of time a read request can take; how many retries are allowed; and soon. The SLA should also define compensation for users if the specifications aren't met. A cloud storage service provider usually offers a tiered service credit plan that gives users credits based on the discrepancy between SLA specifications and the actual service levels delivered.
