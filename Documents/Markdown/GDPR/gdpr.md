# The GDPR and DVerse

I used <https://gdpr-info.eu/> to read the GDPR and based on the information from both the articles and recitals I will make a list of concerns that the DVerse project can touch upon and what can be done to minimize the risk of violating these articles and/or recitals.  
Although I have no experience with dealing with law issues I will try to make it as clear as possible and objective as possible.

For a clarification on what an article or recital means I follow the following definitions from [rsisecurity](https://blog.rsisecurity.com/what-are-gdpr-recitals/) and [TermsFeed](https://www.termsfeed.com/dictionary/gdpr-recital-definition/).  
An article contains the main language of the law with concise requirements outlined.
The recitals help add guidance, context and additional detailed information to help support and clarify the text of the GDPR articles.

I will begin with the articles and try to reason why certain articles will be included in my part of is it necessary to follow for the DVerse project.  Although you should completely follow the GDPR if you aren't going to touch upon these issues why bother with following them is my opinion. The articles that will be touched upon should always be kept in mind and see what can be done to minimize risk.

An interesting note to this is that while reading how the DVerse can comply with it I asked myself how does the Fediverse itself comply with the GDPR which I came out to an article by EUROPEAN DATA PROTECTION SUPERVISOR see the following for the article: <https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2022-07-26-techdispatch-12022-federated-social-media-platforms_en>  
As it goes over what the Fediverse is and what is means. I found an interesting sentence, `many federated platforms share and cache user-generated public content widely and irrespectively of legal requirements on international data transfers.` thus this means that for example Mastodon can cache user-generated content without using the legal requirements on international data transfers. This is something i find not that great thus while I wish that the DVerse project will not go into this path, it can be unavoidable in the long run with talking to other federated systems.

I will begin with Chapter 1 article 3. This concerns what does the GDPR apply to and what not. This is important to keep in mind so you can decide based on the law what you need to do or do not need to do.

## Article 3 Territorial scope

1. This Regulation applies to the processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union or not.
2. This Regulation applies to the processing of personal data of data subjects who are in the Union by a controller or processor not established in the Union, where the processing activities are related to:
   1. the offering of goods or services, irrespective of whether a payment of the data subject is required, to such data subjects in the Union; or
   2. the monitoring of their behavior as far as their behavior takes place within the Union.
3. This Regulation applies to the processing of personal data by a controller not established in the Union, but in a place where Member State law applies by virtue of public international law.

This means that if the DVerse project is live and if a server is running in the Union it should follow the GDPR. Also if it's being processed in the Union. A short example of how this applies can be an Belgian user makes an account for the DVerse project because this user is part of the Union they are subjected to the GDPR and thus because it originated from an Union citizen the laws of the GDPR apply. Now comes an American citizen that also want's to have an account for the DVerse project aside from the american and county laws that should apply if their data comes in contact with a server that is being run in the Union then the GDPR also applies to them.  So this short example shows the side of the processor and then the controller.

Suitable Recitals: 22,23,24,25

## Article 4 Definitions

This article has a long list of what the definitions are that will be called upon in this regulation. I recommend to read at least this article to know more about what certain words mean inside of this regulations.

## Article 5 Principles relating to processing of personal data

This goes into what the rights are with processing of personal data.
For this article everything that will be saved or entered needs to have a purpose. For example if gender is asked for but you are not doing anything with such as statistics or difference in functionality (such as that there is woman's chatroom and no man can enter it).  
It should also be transparent, lawfully and fairly in relation to the data subject. Which means that you can't say what you are not collecting without receiving a penalty if found out. This can be done with an agreement that the user needs to accept.  
1.b says about processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes need to be in accordance with article 89.1, not be considered to be incompatible with the initial purposes (‘purpose limitation’); For this I recommend to read article 89 subsection 1 for the entire details.  
After these sections comes one about accuracy so when the data is no longer needed it be deleted  or rectified without delay. This can be said over when an user deletes their account that the personal info should be deleted without delay. Of course we can keep the non-personal data for longer such as for statistics or looking for intent of hiding dangerous thought (such as how to build a bomb or which cleaning products should not be combined).  
Now with 1.e it does say that when the data is kept in a form which permits identification of data subjects it should not be no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 89.1. This is subjected to implementation of the appropriate technical and organizational measures required by this Regulation in order to safeguard the rights and freedoms of the data subject. Thus if there is a legitimate reason why personal data should be kept longer for the purpose of identification such as I write above such as statistics and intent of questions.
With 1.f this  brings a layer of security that should be implemented and found out how it will be done in the DVerse project as Fediverse can communicate with other entities that could not be in the Union. With also the option to make their own bots.  
As this is a "third-party" entity (Bot or Fediverse server) we should be able to show how we deal with the added security issues that this brings such as that no company is on the top and says what is allowed although there will likely be moderators/admins that do check this but you can't be certain if everything will work out fine. An blaring issue I find myself is that either every bot should be checked by a higher authority than the regular user or a limitation on how users can make something that deals with personal data. For the Fediverse side I have no clear idea what could be done for this as this could be subject to change and not a clear purpose for it has been created.

With the last paragraph it goes about how the controller is responsible for paragraph 1 and should be able to demonstrate compliance.

Suitable Recitals: 39,74

## Article 6 Lawfulness of processing

This article is mostly about consent of the data subject. The processing shall be lawful if at least one of the following apply.

1. The data subject has consented that their personal data for one or more specific purposes can be processed.
2. 1.b is about contracts as we don't deliver contracts this will be skipped
3. Processing is necessary for compliance with a legal obligation to which the controller is subject; This is difficult to create a scenario to which it applies to DVerse. An example of it could be that a company called `DataCompliance Inc` does cloud storage, one of their clients is `Legal Inc` this company handles legal documents for their clients. `Legal Inc` has the legal obligation to retain client documents for a specific period (e.g., seven years) as required by local regulations and professional standards.  `DataCompliance Inc` processes personal data on behalf of `Legal Inc`. This includes storing and managing client documents securely in their cloud servers. The personal data may include names, addresses, case details, and other relevant information. `DataCompliance Inc`'s processing of personal data is necessary for `Legal Inc` to fulfill its legal obligation. Without this processing, `Legal Inc` would be unable to comply with the retention requirements imposed by law. `DataCompliance Inc` relies on Article 6.1.C of the GDPR as the lawful basis for processing. By providing the cloud storage service, they assist `Legal Inc` in meeting its legal obligations.
4. 1.d goes over the vital interest of the data subject to protect them. Such as collecting IP-addresses (for security and analytics purposes) so that it can  prevent malicious activities such as hacking attempts.
5. 1.e goes over how it can help the public interest or in the exercise of official authority vested in the controller. As the DVerse project itself is for the public interest the collection of data is not. Thus for this we can't process the data following the law. But such as that the police asks for the data that was made for an user while doing an investigation we can process it.
6. 1.f goes over if the processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party. Except that when such interest are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data and especially when it's a child. The Fediverse is such third-party for the DVerse state and as we don't have control anymore over the data when it's on that side.

Paragraph 2 Member States may maintain or introduce more specific provisions to adapt the application of the rules of this Regulation with regard to processing for compliance with points (c) and (e) of paragraph 1 by determining more precisely specific requirements for the processing and other measures to ensure lawful and fair processing including for other specific processing situations as provided for in [Chapter IX](https://gdpr-info.eu/chapter-9/).

Paragraph 3 the basis for the processing referred to in point (c) and (e) of paragraph 1 shall be laid down by either Union law or Member State law to which the controller is subject.

Paragraph 4 this paragraph outlines specific cases where processing personal data is considered lawful even without the data subject’s consent.
It provides alternative legal bases for data processing when consent is not applicable or feasible.

Suitable Recitals: 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 171

## Article 7 Conditions for consent

Paragraph 1 When the processing is based on consent. The controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. An example of this is that you have a privacy statement versioned and compare it with the creation of the account to see if based on the privacy statement they signed the processing is also handled in that way or better.

Paragraph 2 If the consent for the data is written, the request for consent shall be presented in a manner which is clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language. Any part of such a declaration which constitutes an infringement of this Regulation shall not be binding.  
Which means so long the DVerse project doesn't do written declarations that constitute to the collection of data that is personal or can be used to identify people this paragraph has nothing to do with the DVerse project.

Paragraph 3 means that when the data subject requests a withdrawal of consent at any given moment. The withdrawal of consent shall not affect the lawfulness of processing based on consent before its withdrawal. Prior to giving consent, the data subject shall be informed thereof. It shall be as easy to withdraw as to give consent.  
Thus with the example of the saving the questions asked and their answers. The data subject shall be informed on how these questions will be saved, how they can withdraw their consent for these questions or delete the history of it. But it should not affect the lawfulness of processing based on consent before its withdrawal. Thus an example being that mysterious/ dangerous or bad-fate questions will need to be found in their history before permanently deleting history. If given those sort of questions the correct authorities should be informed if necessary and not on suspicion of actually committing a crime or plotting one.

Paragraph 4 When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the processing of personal data that is not necessary for the performance of that contract.
With this you can go back on the history of questions asked, based on if the history is automatically saved without consent it will be a problem. While this could be in a privacy statement or terms of service it doesn't automatically mean that the saving of questions is necessary.

Suitable Recitals: 32, 33, 42, 43

## Article 8 Conditions applicable to child's consent in relation to information society services

Although this means that the DVerse project need to regulate how old the user is in a way. Or the conditions that are in this article should not happen in the DVerse project.

Paragraph 1 Where point (a) of Article 6.1 applies, in relation to the offer of information society services directly to a child, the processing of the personal data of a child shall be lawful where the child is at least 16 years old. Where the child is below the age of 16 years, such processing shall be lawful only if and to the extent that consent is given or authorized by the holder of parental responsibility over the child.  
So if the child (<16) has not got a form of any kind where the holder of parental responsibility consents also to this. I recommend that this shall be split in multiple parts where different consent shall need to be given. So far the DVerse project you can ask only questions so a reasonable holder of parental responsibility will likely consent to it but if the DVerse project expands and has more functionality such as chat rooms I advise that therefore also consent needs to be given. A problem with this can be that because the child can handle the device which they connect to the DVerse project a simple form of `If you are <16 years does your "holder of parental responsibility" also consent to you being on this` they can quickly click on yes they consent. Thus either you hold the holder of parental responsibility responsible for the child's mistake or you improve the method of how consent is given to the child.

Paragraph 2 says that the controller shall make reasonable efforts to verify in such cases that consent is given or authorized by the holder of parental responsibility over the child, taking into consideration available technology.  
Thus with this paragraph the simple form of consent is taken out and a more robust system needs to be taken care of. This shall be a hard undertaking and depends on reasonable access to technology to a child (<16) a teen has likely knowledge of certain websites that can generate a temporary email thus sending an email to ask for consent can be not enough in the eye of law. I have no direct recommendations for this as I don't have a reasonable knowledge that the child could have and what is most commonly used. Examples that can be used are phone verification in the form of sms (but a teen probably has their own phone), Payment verification but because this information is not necessarily needed it could be difficult (but a teen can also give their own bank if they know it), Video Call or In-Person Verification is also a option but because the moderators/admin will probably not be paid or is small with larger communities that can be a hassle and take to long to verify. Another downside of Video Call is that a filter can be placed on the call either by the camera itself or a program that can do this.

Paragraph 3 informs you that paragraph 1 shall not affect the general contract law of Member States such as the rules on the validity, formation or effect of a contract in relation to a child. Thus for example a binding contract for payment can not be made with a child.

Suitable Recitals: 38

## Paragraph 9 Processing of special categories of personal data

Paragraph 1 is about data if it's racial or ethnic racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, genetic data, biometric data and data concerning a natural person’s sex life or sexual orientation shall be prohibited.  
If we don't collect this there will be no problem. Or rather I recommend to prohibit to ask for this data and let it be unknown.

Paragraph 2 is that with certain purposes the Paragraph 1 will be not be applied. As I recommend and currently no such information is available or will be asked, this can be excluded for this document.

Paragraph 3 will continue further on Paragrahp 1 about how it may be processed and  for the purposes referred within subparagraph h of paragraph 2 under the responsibility of a professional subject to the obligation of professional secrecy under Union or Member State law or rules established by national competent bodies or by another person also subject to an obligation of secrecy under Union or Member State law or rules established by national competent bodies.

Paragraph 4 Member States may maintain or introduce further conditions, including limitations, with regard to the processing of genetic data, biometric data or data concerning health.  
So long no such information will be asked for we can skip this paragraph but when asked we need to keep this in mind.

Suitable Recitals: 46, 51, 52, 53, 54, 55, 56

## Article 10 Processing of personal data relating to criminal convictions and offenses

As I recommend not to touch this and let members of the DVerse project or participants make bots or functionality that can infringe on this.

But when under orders be carried out only under the control of official authority or when the processing is authorized by Union or Member State law providing for appropriate safeguards for the rights and freedoms of data subjects.

Suitable Recitals: 50

## Article 11 Processing which does not require identification

Paragraph 1

Paragraph 2

Suitable Recitals:
