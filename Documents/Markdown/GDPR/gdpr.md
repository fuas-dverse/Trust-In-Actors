# The GDPR and DVerse

I used <https://gdpr-info.eu/> to read the GDPR and based on the information from both the articles and recitals I will make a list of concerns that the DVerse project can touch upon and what can be done to minimize the risk of violating these articles and/or recitals.  
Although I have no experience with dealing with law issues, I will try to make it as clear as possible and objective as possible.

For a clarification on what an article or recital means I follow the following definitions from [rsisecurity](https://blog.rsisecurity.com/what-are-gdpr-recitals/) and [TermsFeed](https://www.termsfeed.com/dictionary/gdpr-recital-definition/).  
An article contains the main language of the law with concise requirements outlined.
The recitals help add guidance, context, and additional detailed information to help support and clarify the text of the GDPR articles.

I will begin with the articles and try to reason why certain articles will be included in my part of is it necessary to follow for the DVerse project. Although you should completely follow the GDPR if you aren't going to touch upon these issues why bother with following them is my opinion. The articles that will be touched upon should always be kept in mind and see what can be done to minimize risk.

An interesting note to this is that while reading how the DVerse can comply with it I asked myself how the Fediverse complies with the GDPR which I came out to an article by EUROPEAN DATA PROTECTION SUPERVISOR see the following for the article: <https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2022-07-26-techdispatch-12022-federated-social-media-platforms_en>  
As it goes over what the Fediverse is and what is means. I found an interesting sentence, `many federated platforms share and cache user-generated public content widely and irrespectively of legal requirements on international data transfers. ` thus this means that for example Mastodon can cache user-generated content without using the legal requirements on international data transfers. This is something I find not that great thus while I wish that the DVerse project will not go into this path, it can be unavoidable in the long run with talking to other federated systems.

I will begin with Chapter 1 article 3. This concerns what does the GDPR apply to and what not. This is important to keep in mind so you can decide based on the law what you need to do or do not need to do.

## Article 3 Territorial scope

1. This Regulation applies to the processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union or not.
2. This Regulation applies to the processing of personal data of data subjects who are in the Union by a controller or processor not established in the Union, where the processing activities are related to:
   1. the offering of goods or services, irrespective of whether a payment of the data subject is required, to such data subjects in the Union; or
   2. the monitoring of their behavior as far as their behavior takes place within the Union.
3. This Regulation applies to the processing of personal data by a controller not established in the Union, but in a place where Member State law applies by virtue of public international law.

This means that if the DVerse project is live and if a server is running in the Union, it should follow the GDPR. Also, if it's being processed in the Union. A short example of how this applies can be a Belgian user makes an account for the DVerse project because this user is part of the Union, they are subjected to the GDPR and thus because it originated from a Union citizen the laws of the GDPR apply. Now comes an American citizen that also wants to have an account for the DVerse project aside from the American and county laws that should apply if their data comes in contact with a server that is being run in the Union then the GDPR also applies to them.  So, this short example shows the side of the processor and then the controller.

Suitable Recitals: 22,23,24,25

## Article 4 Definitions

This article has a long list of what the definitions are that will be called upon in this regulation. I recommend reading at least this article to know more about what certain words mean inside of this regulation.

## Article 5 Principles relating to processing of personal data

This goes into what the rights are with processing of personal data.
For this article everything that will be saved or entered needs to have a purpose. For example, if gender is asked for but you are not doing anything with such as statistics or difference in functionality (such as that there is woman's chatroom, and no man can enter it).  
It should also be transparent, lawfully, and fairly in relation to the data subject. Which means that you can't say what you are not collecting without receiving a penalty if found out. This can be done with an agreement that the user needs to accept.  
1.b says about processing for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes need to be in accordance with article 89.1, not be incompatible with the initial purposes (‘purpose limitation’); For this I recommend reading article 89 subsection 1 for the entire details.  
After these sections comes one about accuracy so when the data is no longer needed it be deleted or rectified without delay. This can be said over when a user deletes their account that the personal info should be deleted without delay. Of course, we can keep the non-personal data for longer such as for statistics or looking for intent of hiding dangerous thought (such as how to build a bomb or which cleaning products should not be combined).  
Now with 1.e it does say that when the data is kept in a form which permits identification of data subjects it should not be no longer than is necessary for the purposes for which the personal data are processed; personal data may be stored for longer periods insofar as the personal data will be processed solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 89.1. This is subjected to implementation of the appropriate technical and organizational measures required by this Regulation in order to safeguard the rights and freedoms of the data subject. Thus, if there is a legitimate reason why personal data should be kept longer for the purpose of identification such as I write above such as statistics and intent of questions.
With 1.f this brings a layer of security that should be implemented and found out how it will be done in the DVerse project as Fediverse can communicate with other entities that could not be in the Union. With also the option to make their own bots.  
As this is a "third-party" entity (Bot or Fediverse server) we should be able to show how we deal with the added security issues that this brings such as that no company is on the top and says what is allowed although there will likely be moderators/admins that do check this, but you can't be certain if everything will work out fine. A blaring issue I find myself is that either every bot should be checked by a higher authority than the regular user or a limitation on how users can make something that deals with personal data. For the Fediverse side I have no clear idea what could be done for this as this could be subject to change and not a clear purpose for it has been created.

With the last paragraph it goes about how the controller is responsible for paragraph 1 and should be able to demonstrate compliance.

Suitable Recitals: 39,74

## Article 6 Lawfulness of processing

This article is mostly about consent of the data subject. The processing shall be lawful if at least one of the following apply.

1. The data subject has consented that their personal data for one or more specific purposes can be processed.
2. 1.b is about contracts as we don't deliver contracts this will be skipped
3. Processing is necessary for compliance with a legal obligation to which the controller is subject; This is difficult to create a scenario to which it applies to DVerse. An example of it could be that a company called `DataCompliance Inc` does cloud storage, one of their clients is `Legal Inc` this company handles legal documents for their clients. `Legal Inc` has the legal obligation to retain client documents for a specific period (e.g., seven years) as required by local regulations and professional standards.  `DataCompliance Inc` processes personal data on behalf of `Legal Inc`. This includes storing and managing client documents securely in their cloud servers. The personal data may include names, addresses, case details, and other relevant information. `DataCompliance Inc`'s processing of personal data is necessary for `Legal Inc` to fulfill its legal obligation. Without this processing, `Legal Inc` would be unable to comply with the retention requirements imposed by law. `DataCompliance Inc` relies on Article 6.1.C of the GDPR as the lawful basis for processing. By providing the cloud storage service, they assist `Legal Inc` in meeting its legal obligations.
4. 1.d goes over the vital interest of the data subject to protect them. Such as collecting IP-addresses (for security and analytics purposes) so that it can prevent malicious activities such as hacking attempts.
5. 1.e goes over how it can help the public interest or in the exercise of official authority vested in the controller. As the DVerse project itself is for the public interest the collection of data is not. Thus, for this we can't process the data following the law. But such as that the police ask for the data that was made for a user while doing an investigation, we can process it.
6. 1.f goes over if the processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party. Except that when such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data and especially when it's a child. The Fediverse is such third-party for the DVerse state and as we don't have control anymore over the data when it's on that side.

Paragraph 2 Member States may maintain or introduce more specific provisions to adapt the application of the rules of this Regulation regarding processing for compliance with points (c) and (e) of paragraph 1 by determining more precisely specific requirements for the processing and other measures to ensure lawful and fair processing including for other specific processing situations as provided for in [Chapter IX](https://gdpr-info.eu/chapter-9/).

Paragraph 3 the basis for the processing referred to in point (c) and (e) of paragraph 1 shall be laid down by either Union law or Member State law to which the controller is subject.

Paragraph 4 this paragraph outlines specific cases where processing personal data is considered lawful even without the data subject’s consent.
It provides alternative legal bases for data processing when consent is not applicable or feasible.

Suitable Recitals: 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 171

## Article 7 Conditions for consent

Paragraph 1 When the processing is based on consent. The controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data. An example of this is that you have a privacy statement versioned and compare it with the creation of the account to see if based on the privacy statement they signed the processing is also handled in that way or better.

Paragraph 2 If the consent for the data is written, the request for consent shall be presented in a manner which is clearly distinguishable from the other matters, in an intelligible and easily accessible form, using clear and plain language. Any part of such a declaration which constitutes an infringement of this Regulation shall not be binding.  
Which means so long the DVerse project doesn't do written declarations that constitute to the collection of data that is personal or can be used to identify people this paragraph has nothing to do with the DVerse project.

Paragraph 3 means that when the data subject requests a withdrawal of consent at any given moment. The withdrawal of consent shall not affect the lawfulness of processing based on consent before its withdrawal. Prior to giving consent, the data subject shall be informed thereof. It shall be as easy to withdraw as to give consent.  
Thus, with the example of the saving the questions asked and their answers. The data subject shall be informed on how these questions will be saved, how they can withdraw their consent for these questions or delete the history of it. But it should not affect the lawfulness of processing based on consent before its withdrawal. Thus, an example being that mysterious/ dangerous or bad-fate questions will need to be found in their history before permanently deleting history. If given those sorts of questions the correct authorities should be informed if necessary and not on suspicion of committing a crime or plotting one.

Paragraph 4 When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the processing of personal data that is not necessary for the performance of that contract.
With this you can go back on the history of questions asked, based on if the history is automatically saved without consent it will be a problem. While this could be in a privacy statement or terms of service it doesn't automatically mean that the saving of questions is necessary.

Suitable Recitals: 32, 33, 42, 43

## Article 8 Conditions applicable to child's consent in relation to information society services

Although this means that the DVerse project need to regulate how old the user is in a way. Or the conditions that are in this article should not happen in the DVerse project.

Paragraph 1 Where point (a) of Article 6.1 applies, in relation to the offer of information society services directly to a child, the processing of the personal data of a child shall be lawful where the child is at least 16 years old. Where the child is below the age of 16 years, such processing shall be lawful only if and to the extent that consent is given or authorized by the holder of parental responsibility over the child.  
So, if the child (<16) has not got a form of any kind where the holder of parental responsibility consents also to this. I recommend that this shall be split in multiple parts where different consent shall need to be given. So far, the DVerse project you can ask only questions so a reasonable holder of parental responsibility will likely consent to it but if the DVerse project expands and has more functionality such as chat rooms I advise that therefore also consent needs to be given. A problem with this can be that because the child can handle the device which they connect to the DVerse project a simple form of `If you are <16 years does your "holder of parental responsibility" also consent to you being on this` they can quickly click on yes, they consent. Thus, either you hold the holder of parental responsibility responsible for the child's mistake or you improve the method of how consent is given to the child.

Paragraph 2 says that the controller shall make reasonable efforts to verify in such cases that consent is given or authorized by the holder of parental responsibility over the child, taking into consideration available technology.  
Thus, with this paragraph the simple form of consent is taken out and a more robust system needs to be taken care of. This shall be a hard undertaking and depends on reasonable access to technology to a child (<16) a teen has likely knowledge of certain websites that can generate a temporary email thus sending an email to ask for consent can be not enough in the eye of law. I have no direct recommendations for this as I don't have a reasonable knowledge that the child could have and what is most used. Examples that can be used are phone verification in the form of SMS (but a teen probably has their own phone), Payment verification but because this information is not necessarily needed it could be difficult (but a teen can also give their own bank if they know it), Video Call or In-Person Verification is also an option but because the moderators/admin will probably not be paid or is small with larger communities that can be a hassle and take too long to verify. Another downside of Video Call is that a filter can be placed on the call either by the camera itself or a program that can do this.

Paragraph 3 informs you that paragraph 1 shall not affect the general contract law of Member States such as the rules on the validity, formation, or effect of a contract in relation to a child. Thus, for example a binding contract for payment cannot be made with a child.

Suitable Recitals: 38

## Paragraph 9 Processing of special categories of personal data

Paragraph 1 is about data if it's racial or ethnic racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, genetic data, biometric data, and data concerning a natural person’s sex life or sexual orientation shall be prohibited.  
If we don't collect this there will be no problem. Or rather I recommend prohibiting to ask for this data and let it be unknown.

Paragraph 2 is that with certain purposes the Paragraph 1 will not be applied. As I recommend and currently no such information is available or will be asked, this can be excluded for this document.

Paragraph 3 will continue further on Paragraph 1 about how it may be processed and for the purposes referred within subparagraph h of paragraph 2 under the responsibility of a professional subject to the obligation of professional secrecy under Union or Member State law or rules established by national competent bodies or by another person also subject to an obligation of secrecy under Union or Member State law or rules established by national competent bodies.

Paragraph 4 Member States may maintain or introduce further conditions, including limitations, regarding the processing of genetic data, biometric data or data concerning health.  
So long no such information will be asked for we can skip this paragraph but when asked we need to keep this in mind.

Suitable Recitals: 46, 51, 52, 53, 54, 55, 56

## Article 10 Processing of personal data relating to criminal convictions and offenses

As I recommend not to touch this and let members of the DVerse project, or participants make bots or functionality that can infringe on this.

But when under orders be carried out only under the control of official authority or when the processing is authorized by Union or Member State law providing for appropriate safeguards for the rights and freedoms of data subjects.

Suitable Recitals: 50

## Article 11 Processing which does not require identification

Paragraph 1 is if the purposes for which a controller processes personal data do not or do no longer require the identification of a data subject by the controller, the controller shall not be obliged to maintain, acquire, or process additional information in order to identify the data subject for the sole purpose of complying with this Regulation.  
So, if the data is no longer needed you don't need to be obliged to maintain, acquire, or process additional information to comply with the GDPR.

Paragraph 2 is when the controller is able to demonstrate that it is not in a position to identify the data subject, the controller shall inform the data subject accordingly, if possible, in the case of paragraph 1. In such cases Articles 15 to 20 shall not apply. Unless the data subject for the purpose of exercising their rights under those articles, provides additional information enabling his or her identification.  
With having to do with paragraph 1 we can skip over the articles 15 to 20.  Unless the data subject wants to exercise their right and provides additional information enabling their identification.

Suitable Recitals: 57

## Article 12 Transparent information, communication, and modalities for the exercise of the rights of the data subject

Paragraph 1 the controller shall take appropriate measures to provide any information referred to in Articles 13 and 14 and any communication under Articles 15 to 22 and 34 relating to processing to the data subject in a concise, transparent, intelligible, and easily accessible form, using clear and plain language, in particular for any information addressed specifically to a child. Furthermore, it shall be provided in writing or by other means, including, where appropriate, by electronic means. When requested by the data subject, the information may be provided orally, provided that the identity of the data subject is proven by other means.  
For this paragraph nothing comes to mind for what to do, just send an email in plain language if there is any problem.

Paragraph 2 The controller shall facilitate the exercise of data subject rights under Articles 15 to 22. In the cases referred to in Article 11 paragraph 2, the controller shall not refuse to act on the request of the data subject for exercising his or her rights under Articles 15 to 22, unless the controller demonstrates that it is not in a position to identify the data subject.  
You need to follow the right under Articles 15 to 22. Unless the data subject is not possible to identify and can be demonstrated.

Paragraph 3 The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request. This period may be extended 2 months when necessary, taking into account the complexity and number of the requests. The controller shall inform the data subject of any such extension within one month of receipt of the request, together with the reasons for the delay. Where the data subject makes the request by electronic form means, the information shall be provided by electronic means unless otherwise requested by the data subject.  
If a data subject asks for their information such as the routes that have been taken. Then we can provide this if the DVerse project wants to save the route of information otherwise it will be impossible to trace the route.

Paragraph 4 if the controller does not act on the request of the data subject, the controller shall inform the data subject without delay and at the latest within one month of receipt of the request of the reasons for not taking action. With the possibility of lodging a complaint with a supervisory authority and seeking a judicial remedy.  
If we go back to the example of the route of information if this is not saved, then we cannot fulfill this request and thus need to specify where they can go to lodge a complaint.

Paragraph 5 Information provided under Articles 13 and 14 and any communication and any actions taken under Articles 15 to 22 and 34 shall be provided free of charge. But if the requests from the data subject are manifestly unfounded or excessive, in particular because of their repetitive character, the controller may either: charge a reasonable fee taking into account the administrative costs of providing the information or communication or taking the action requested; or refuse to act on the request.  
The controller shall bear the burden of demonstrating the manifestly unfounded or excessive character of the request.  
With this paragraph you need to provide the information requested for free but if it's repetitive you can put a price on it for administrative costs.

Paragraph 6 Without prejudice to Article 11, where the controller has reasonable doubts concerning the identity of the natural person making the request referred to in Articles 15 to 21, the controller may request the provision of additional information necessary to confirm the identity of the data subject.  
If needed, you can request more information to identify the person, but it should not cross the prejudice of Article 11.

Paragraph 7 The information to be provided to data subjects pursuant to Articles 13 and 14 may be provided in combination with standardized icons in order to give in an easily visible, intelligible, and clearly legible manner a meaningful overview of the intended processing. Where the icons are presented electronically, they shall be machine-readable.  
We can use icons, but they should be standardized, easily visible, intelligible, and clearly legible manner. With the presentation electronically you can think about that a screen reader can read this.

Paragraph 8 is about the Commission and that are empowered to adopt delegated acts in accordance with Article 92 for the purpose of determining the information to be presented by the icons and the procedures for providing standardized icons.

Suitable Recitals: 58, 59, 60, 73

## Article 13 Information to be provided where personal data are collected from the data subject

Paragraph 1 Where personal data relating to a data subject are collected from the data subject, the controller shall, at the time when personal data are obtained, provide the data subject with:

1. the identity and the contact details of the controller and, where applicable, of the controller’s representative.
1. the contact details of the data protection officer, where applicable.
1. the purposes of the processing
1. where the processing is based on point (f) of Article 6 paragraph 1
1. the recipients or categories of recipients of the personal data, if any.
1. where applicable, the fact that the controller intends to transfer personal data.

I recommend for this paragraph to have a standard way of getting this information and put in a terms of service or other document the points of the information that are brought in this section.

Paragraph 2 In addition to the information referred to in paragraph 1, the controller shall, at the time when personal data are obtained, provide the data subject with the following further information necessary to ensure fair and transparent processing:

1. the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period.
1. the existence of the right to request, access to and rectification or erasure of personal data, restriction of processing concerning the data subject, object to processing as well as the right to data portability.
1. where the processing is based on point (a) of Article 6 paragraph 1 or point (a) of Article 9 paragraph 2, the existence of the right to withdraw consent at any time
1. the right to lodge a complaint with a supervisory authority.
1. whether the provision of personal data is a statutory or contractual requirement, or a requirement necessary to enter into a contract. As well as possible consequences of failure to provide such data.
1. the existence of automated decision-making, including profiling, referred to in Article 22 paragraph 1 and 4. As well as the significance and the envisaged consequences of such processing for the data subject.

For this I recommend the extension on the recommendation of paragraph 1, with how long things will be stored or reason, how the data subject can do their rights and complaint. The contractual/statutory is not for this project based on the current situation.

Paragraph 3 Where the controller intends to further process the personal data for a purpose other than that for which the personal data were collected, the controller shall provide further information why they want to process it and what they want to process to the data subject.  
This means if you don't process information without a purpose you don't need to follow it. So, I recommend that no further processing of personal data will happen. Before asking this personal data, a purpose needs to be thought about and based on that needs consent be given.

Paragraph 4, Paragraphs 1, 2 and 3 shall not apply where and insofar as the data subject already has the information.  
So, if the data subject already has the information you don't need to investigate the above paragraphs.

Suitable Recitals: 60, 61, 62

## Article 14 Information to be provided where personal data have not been obtained from the data subject

Paragraph 1 Where personal data have not been obtained from the data subject, the controller shall provide the data subject with the following information:

1. the identity and the contact details of the controller and, where applicable, of the controller’s representative.
1. the contact details of the data protection officer, where applicable.
1. the purposes of the processing for which the personal data are intended as well as the legal basis for the processing.
1. the categories of personal data concerned.
1. the recipients or categories of recipients of the personal data, if any.
1. where applicable, the fact that the controller intends to transfer personal data.

I recommend for this paragraph to have a standard way of getting this information and put in a terms of service or other document the points of the information that are brought in this section.

Paragraph 2 In addition to the information referred to in paragraph 1, the controller shall provide the data subject with the following information necessary to ensure fair and transparent processing in respect of the data subject:

1. the period for which the personal data will be stored, or if that is not possible, the criteria used to determine that period.
1. where the processing is based on point (f) of Article 6 paragraph 1
1. the existence of the right to request, access to and rectification or erasure of personal data, restriction of processing concerning the data subject, object to processing as well as the right to data portability.
1. where the processing is based on point (a) of Article 6 paragraph 1 or point (a) of Article 9 paragraph 2, the existence of the right to withdraw consent at any time
1. the right to lodge a complaint with a supervisory authority.
1. from which source the personal data originate, and if applicable, whether it came from publicly accessible sources.
1. the existence of automated decision-making, including profiling, referred to in Article 22 paragraph 1 and 4. As well as the significance and the envisaged consequences of such processing for the data subject.

For this I recommend the extension on the recommendation of paragraph 1, with how long things will be stored or reason, how the data subject can do their rights and complaint.

Paragraph 3 The controller shall provide the information referred to in paragraphs 1 and 2, in reasonable period after obtaining the personal data, but at the latest within one month, having regard to the specific circumstances in which the personal data are processed; if the personal data are to be used for communication with the data subject, at the latest at the time of the first communication to that data subject; or
if a disclosure to another recipient is envisaged, at the latest when the personal data are first disclosed.

Thus, when a request comes for their information, you need to send it at the latest moment of a month unless there is an exception. If the personal data is used for communication or if a disclosure to another recipient is envisaged.

Paragraph 4 Where the controller intends to further process the personal data for a purpose other than that for which the personal data were collected, the controller shall provide further information why they want to process it and what they want to process to the data subject. As referred in paragraph 2.  
This means if you don't process information without a purpose you don't need to follow it. So, I recommend that no further processing of personal data will happen. Before asking this personal data, a purpose needs to be thought about and based on that needs consent be given.

Paragraph 5 Paragraphs 1 to 4 shall not apply where and insofar as:

1. the data subject already has the information.
1. the provision of such information proves impossible or would involve a disproportionate effort
1. obtaining or disclosure is expressly laid down by Union or Member State law to which the controller is subject and which provides appropriate measures to protect the data subject’s legitimate interests.
1. where the personal data must remain confidential subject to an obligation of professional secrecy regulated by Union or Member State law, including a statutory obligation of secrecy.

As we likely not have confidential information, we can skip those exceptions and think about that those exceptions will not exist for this project. If no implementation is made for example the route of messages, then it will take a long time or impossible/disproportionate effort to get this information. While the data subject already has the information will be easily taken care of with a table of when they last requested this information and what an appropriate time is that the data subject can request this information again.

Suitable Recitals: 60, 61, 62

## Article 15 Right of access by the data subject

Paragraph 1 The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information:

1. the purposes of the processing.
1. the categories of personal data concerned.
1. the recipients or categories of recipient to whom the personal data have been or will be disclosed, in particular recipients in third countries or international organizations.
1. where possible, the envisaged period for which the personal data will be stored, or, if not possible, the criteria used to determine that period.
1. the existence of the right to request from the controller rectification or erasure of personal data or restriction of processing of personal data concerning the data subject or to object to such processing.
1. the right to lodge a complaint with a supervisory authority.
1. where the personal data are not collected from the data subject, any available information as to their source.
1. the existence of automated decision-making, including profiling, referred to in Article 22 paragraph 1 and 4 and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject.

With this I recommend keeping this in mind and make some options functional or written to how they can exercise these rights. Or where they can get this information.

Paragraph 2 Where personal data are transferred to a third country or to an international organization, the data subject shall have the right to be informed of the appropriate safeguards pursuant to Article 46 relating to the transfer.  
As this project is Federated meaning that everybody could be able to set their own service of this project. And that they can communicate with other entities of the same type (Federated) as it's possible that such server is related to the third country, we need to follow Article 46 when data is transferred over.

Paragraph 3 The controller shall provide a copy of the personal data undergoing processing. For any further copies requested by the data subject, the controller may charge a reasonable fee based on administrative costs. Where the data subject makes the request by electronic means, and unless otherwise requested by the data subject, the information shall be provided in a commonly used electronic form.  
In short, my recommendations for this are make a table of sorts that the admin/moderator can look in and provide the free copy of personal data. The reasonable price is dependent on the owner of the server, and I have no recommendations of price. Furthermore, I recommend sending it via email either written in the body of it or in a separate pdf document or other easily accessible document (not dependent on OS).

Paragraph 4 The right to obtain a copy referred to in paragraph 3 shall not adversely affect the rights and freedoms of others.  
With this paragraph I can't recommend anything meaningful and will say to keep in mind that it should not affect other people.

Suitable Recitals: 63, 64

## Article 16 Right to rectification

Paragraph 1 The data subject shall have the right to obtain from the controller without undue delay the rectification of inaccurate personal data concerning him or her. Taking into account the purposes of the processing, the data subject shall have the right to have incomplete personal data completed, including by means of providing a supplementary statement.  
So, without undue delay if somebody wants to rectification their personal data they can. With processing they have the right to have their incomplete personal data be completed.

Suitable Recitals: 65

## Article 17 Right to erasure (‘right to be forgotten’)

Paragraph 1 The data subject has the right to obtain from the controller the erasure of personal data concerning him or her without undue delay and the controller shall have the obligation to erase personal data without undue delay where one of the following grounds applies:

1. the personal data are no longer necessary in relation to the purposes for which they were collected or otherwise processed.
1. the data subject withdraws consent on which the processing is based according to point (a) of Article 6 paragraph 1, or point (a) of Article 9 paragraph 2, and where there is no other legal ground for the processing.
1. the data subject objects to the processing pursuant to Article 21 paragraph 1 and there are no overriding legitimate grounds for the processing, or the data subject objects to the processing pursuant to Article 21 paragraph 2.
1. the personal data have been unlawfully processed.
1. the personal data must be erased for compliance with a legal obligation in Union or Member State law to which the controller is subject.
1. the personal data have been collected in relation to the offer of information society services referred to in Article 8 paragraph 1.

Although it says `when no longer necessary` this depends on a condition why it needs to be stored for so long.
Furthermore, when asked by an authority or unlawfully processed, I recommend deleting it immediately.  
In the end try to delete the information as soon as possible when no longer needed and don't have non-personal data connected to personal data as the data can be used for other purposes. An example being commonly asked questions, or the category that is most used.

Paragraph 2 goes about the personal data is public and is obliged pursuant to paragraph 1 to erase the personal data, the controller, taking account of available technology and the cost of implementation, shall take reasonable steps, including technical measures, to inform controllers which are processing the personal data that the data subject has requested the erasure by such controllers of any links to, or copy or replication of, those personal data.

So as this is directly connected to the Fediverse idea of having public information that can be accessed via ActivityPub, I recommend finding out how other media is doing this such as Mastodon. But as this is not only run by professional people I furthermore recommend sending as little personal data as possible to other controllers, so the erasure of data is easier to do.

Paragraph 3 paragraphs 1 and 2 shall not apply to the extent that processing is necessary:

1. for exercising the right of freedom of expression and information.
1. for compliance with a legal obligation which requires processing by Union or Member State law to which the controller is subject or for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller.
1. for reasons of public interest in the area of public health in accordance with points (h) and (i) of Article 9 paragraph 2 as well as Article 9 paragraph 3.
1. for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 89 paragraph 1
1. for the establishment, exercise, or defense of legal claims.

As the first point is quite ambiguous to which it will apply, I will recommend to not process this exception. As the project is not subject to legal obligations, exercise of official authority. You could say that it's in the public interest but with the current data I don't see where it applies for this. For the other points I only think that the last point of the exercise or defense of legal claims can be used for this project as I have made clear multiple times in this document with weird or dangerous questions this can be done.

Suitable Recitals: 65, 66

## Article 18 Right to restriction of processing

Paragraph 1 The data subject shall have the right to obtain from the controller restriction of processing where one of the following applies:

1. the accuracy of the personal data is contested by the data subject, for a period enabling the controller to verify the accuracy of the personal data.
1. the processing is unlawful, and the data subject opposes the erasure of the personal data and requests the restriction of their use instead.
1. the controller no longer needs the personal data for the purposes of the processing, but they are required by the data subject for the establishment, exercise, or defense of legal claims.
1. the data subject has objected to processing pursuant to Article 21 paragraph 1 pending the verification whether the legitimate grounds of the controller override those of the data subject.

For this paragraph I recommend to at least know that data can be restricted. For the individual restrictions.  
The accuracy is fine and can happen, but I do not know in which context currently.  
If it's unlawful then in the first place no processing should happen.  
I do know that with our system a quasi-alibi could happen that is if questions asked are saved and timestamped. Furthermore, if the controller of the DVerse platform does happen to go to authorities for weird/questionable questions then it will also fall under this.  
For the last one I do not think there will be a time that the controller will have legitimate grounds for processing. But when objected to for the processing of data just keep it restricted.  

Now for how you can do this for example have a column where you can tick on, so it makes the data restricted. Or save it in a separate table/database. Other ideas are welcome, but it will likely still come to the same outcome (something with the database data).

Paragraph 2 Where processing has been restricted under paragraph 1, such personal data shall, with the exception of storage, processed under data subjects’ consent, establishment, exercise, or defense of legal claims, for the protection of the rights of another natural or legal person, or reasons of important public interest of the Union or of a Member State.

I recommend that you will only do it all except consent for the data subject as I do not believe there needs to be a reason to process this other than the other exceptions. As personal data will be less exchanged than other information.

Paragraph 3 A data subject who has obtained restriction of processing pursuant to paragraph 1 shall be informed by the controller before the restriction of processing is lifted.  
I recommend having a good reason to lift the restriction of processing and before lifting it a day (or so) send an email to inform the data subject.

Suitable Recitals: 67

## Article 19 Notification obligation regarding rectification or erasure of personal data or restriction of processing

Paragraph 1 The controller shall communicate any rectification or erasure of personal data or restriction of processing carried out in accordance with Article 16, Article 17(1), and Article 18 to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller shall inform the data subject about those recipients if the data subject requests it.

I recommend communicating each rectification or erasure of personal data or restriction of processing to the data subject and recipient.

Suitable Recitals: 66

## Article 20 Right to data portability

Paragraph 1 The data subject shall have the right to receive the personal data concerning him or her, which he or she has provided to a controller, in a structured, commonly used, and machine-readable format. The data subject also has the right to transmit those data to another controller without hindrance from the controller to which the personal data have been provided, where:

1. the processing is based on consent pursuant to point (a) of Article 6 paragraph 1 or point (a) of Article 9 paragraph 2 or on a contract pursuant to point (b) of Article 6 paragraph 1.
1. processing is carried out by automated means.

I recommend putting the data in a JSON (like) format or comma/tab separated. But this is so long that the data is not too long. If it's indeed long I recommend that you use another format like PDF, but I'm not so sure if it will be machine-readable.

Paragraph 2 In exercising their right to data portability pursuant to paragraph 1, the data subject shall have the right to have the personal data transmitted directly from one controller to another, where technically feasible.  
I recommend if it's possible if they want to move their account to another DVerse host it should be possible.  
Furthermore, if it can be done to send to other instances (Mastodon for example) in the Fediverse.

Paragraph 3 the exercise of the right referred to in paragraph 1 of this Article shall be without prejudice to Article 17. That right shall not apply to processing necessary for the performance of a task carried out in the public interest or in the exercise of official authority.  
Unless article 17 is in action we need to follow this right. It also may not hinder the right or limit it. As there will likely no public interest for the data, I recommend to only not do it under official authority.

Paragraph 4 The right referred to in paragraph 1 shall not adversely affect the rights and freedoms of others.
This is straight forward as it should not limit the other rights or affect them. The best way to solve this is to check rules that will be implemented that they will not affect or limit the rights of the data subject.

Suitable Recitals: 68

## Article 21 Right to object

Paragraph 1 The data subject shall have the right to object, on grounds relating to his or her particular situation, at any time to processing of personal data concerning him or her which is based on point (e) or (f) of Article 6 paragraph 1, including profiling based on those provisions.  
Furthermore, the controller shall no longer process the personal data unless the controller demonstrates compelling legitimate grounds for the processing which override the interests, rights, and freedoms of the data subject or for the establishment, exercise, or defense of legal claims.

I recommend making it clear to the data subject how they can object to how their data is used and for the purposes. As I see no legitimate grounds that could override the interest of the data subject, I will say only under legal claims you will have the right to process the data again.

Paragraph 2 is about how processing of personal data for marketing purposes they have the right to object at any moment, which includes profiling to the extent that it is related to such direct marketing.  
I recommend that when a host of the DVerse platform implement advertisements that they will follow this rule and either do not use any personal data or have a `opt-in`/`opt-out` so the data subject can request that their data will not be used.

Paragraph 3 Where the data subject objects to processing for direct marketing purposes, the personal data shall no longer be processed for such purposes.  
As talked in paragraph 2 of this article, I recommend to just don't use the personal data.

Paragraph 4 At the latest at the time of the first communication with the data subject, the right referred to in paragraphs 1 and 2 shall be explicitly brought to the attention of the data subject and shall be presented clearly and separately from any other information.  
For this paragraph just make sure to let the data subject know how they can exercise their right in clear language such as a page with only this information of a separate header that says how you can exercise this right.

Paragraph 5 in the context of the use of information society services, and notwithstanding Directive 2002/58/EC, the data subject may exercise his or her right to object by automated means using technical specifications.  
For this the data subject can automated systems or platforms to communicate their objection to the processing of their data.

Paragraph 6 is about processing for historical or scientific research purposes or statistical purposes pursuant to Article 89 paragraph 1.  
As this is not something that is applicable to this project, I will not recommend anything.

Suitable Recitals: 69, 70

## Article 22 Automated individual decision-making, including profiling

Paragraph 1 The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her.  
I recommend making sure that no decision is based solely on automated processing, or that should significantly affect the data subject.

Paragraph 2 paragraph 1 shall not apply when the decision:

1. is necessary for entering into, or performance of, a contract between the data subject and a data controller.
1. is authorized by Union or Member State law.
1. is based on the data subject’s explicit consent.

Only if the signing-up to the platform or having a leader like (moderator/admin) position, is considered contract then I approve this exception.  
Authorized personal is something I recommend to just follow.  
Furthermore, I do not see a use case where we need to ask for consent of the data subject after the account making that will process information that makes a decision or will significantly affects them.

Paragraph 3 In the cases referred to in points (a) and (c) of paragraph 2, the data controller shall implement suitable measures to safeguard the data subject’s rights and freedoms and legitimate interests, at least the right to obtain human intervention on the part of the controller, to express their point of view and to contest the decision.  
I recommend making a way so a person can intervene between the exchange of data in the system. Furthermore, suitable measures need to be found that can safeguard the data subject.

Paragraph 4 Decisions referred to in paragraph 2 shall not be based on special categories of personal data referred to in Article 9 paragraph 1, unless point (a) or (g) of Article 9 paragraph 2 applies and suitable measures to safeguard the data subject’s rights and freedoms and legitimate interests are in place.  
I recommend making sure that the decisions based on the data are only made under special categories, with their appropriate safeguards in place.

Suitable Recitals: 71, 72, 91

## Article 23 Restrictions

Paragraph 1 is about how the Union or Member State law to which the data controller or processor is subject may restrict the controller with way of a legislative measure the scope of the obligations and rights provided for in Articles 12 to 22 and Article 34, as well as Article 5.

I recommend following Union or Member State law where the data controller or processor is subject to.

Paragraph 2 extends paragraph 1 with specific provisions where it relates to.  
For this I recommend reading it on your own time and find the restrictions that apply for the part of the project that you or/and others are working on.

Suitable Recitals: 73

## Article 24 Responsibility of the controller

Paragraph 1 taking into account the nature, scope, context, and purposes of processing as well as the risks of varying likelihood and severity for the rights and freedoms of natural persons, the controller shall implement appropriate technical and organizational measures to ensure and to be able to demonstrate that processing is performed in accordance with this Regulation. Those measures shall be reviewed and updated where necessary.  
An example of a measure to make sure that the security will be up to date is with implementing OWASP top 10, Authorization for sensitive functionalities, writing likelihood and severity of things that could happen within the project. As the Fediverse made of tiny organizations that are likely being managed in different ways I cannot have clear organizational measures that could be made globally other than not undermining the security provided in the basic package of the platform.  
For review I recommend doing it on your own and then a third party that will look through it.

Paragraph 2 Where proportionate in relation to processing activities, the measures referred to in paragraph 1 shall include the implementation of appropriate data protection policies by the controller.
I recommend anonymization of data when needed so there will be some security benefit when processing activities. Furthermore, other parts that can help the data protection like the database security and communication I recommend looking into.

Paragraph 3 Adherence to approved codes of conduct as referred to in Article 40 or approved certification mechanisms as referred to in Article 42 may be used as an element by which to demonstrate compliance with the obligations of the controller.  
For this you can use the referenced articles so you can get certification that you are able to show that compliance is done.

Suitable Recitals: 74, 75, 76, 77

## Article 25 Data protection by design and by default

Paragraph 1 Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for rights and freedoms of natural persons posed by the processing, the controller shall, both at the time of the determination of the means for processing and at the time of the processing itself, implement appropriate technical and organizational measures, which are designed to implement data-protection principles,  in an effective manner and to integrate the necessary safeguards into the processing in order to meet the requirements of this Regulation and protect the rights of data subjects.  
In short, I recommend adding pseudonymization and data minimization for this paragraph.

Paragraph 2 the controller shall implement appropriate technical and organizational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed.  
That obligation applies to the amount of personal data collected, the extent of their processing, the period of their storage and their accessibility. In particular, such measures shall ensure that by default personal data are not made accessible without the individual’s intervention to an indefinite number of natural persons.  

For this I recommend that when you get something from the database or/and Kafka that you only get what you need such as when you need to find a topic you only look at the keywords or the vectors. For Kafka is it then only the content of the message and not the extra information attached to it. Furthermore, that the messages (Kafka or otherwise) will not be kept indefinitely an example is that with sending updates /live checks that these messages will be deleted in a day or a week at most. As for accessible to an indefinite number of natural persons there needs to be a way where you both have the individual has intervention that they can do and somewhere they don't be combined in a way that the DVerse project will not be in trouble for it.

Paragraph 3 An approved certification mechanism pursuant to Article 42 may be used as an element to demonstrate compliance with the requirements set out in paragraphs 1 and 2 of this Article.  
For this I recommend that you just investigate how the certification works and if you want it.

Suitable Recitals: 78

## Article 26 Joint controllers

Paragraph 1 means that you can have multiple controllers and have joint responsibilities. This needs to be done in a transparent manner. They may also designate a contact point for the data subjects.  
As for this paragraph because the Fediverse can be understood as having joint responsibilities we can say that the owner/host where the account originates from is the contact point and that they need to take the brunt of the responsibilities for this account.

Paragraph 2 The arrangement referred to in paragraph 1 shall duly reflect the respective roles and relationships of the joint controllers vis-à-vis the data subjects. The essence of the arrangement shall be made available to the data subject.  
Thus, as said in the previous paragraph the recommendation is to have the host/owner of the originated account will take most of the tasks and this arrangement shall be written down so the data subject can read this arrangement at any time.

Paragraph 3 Irrespective of the terms of the arrangement referred to in paragraph 1, the data subject may exercise his or her rights under this Regulation in respect of and against each of the controllers.  
In short, the data subject can exercise their rights irrespective of what agreement there is.

Suitable Recitals: 58, 79

## Article 27 Representatives of controllers or processors not established in the Union

Paragraph 1 Where Article 3 paragraph 2 applies, the controller or the processor shall designate in writing a representative in the Union.  
Thus, when article 3 paragraph 2 is being used the DVerse project need to designate a representative.

Paragraph 2 The obligation laid down in paragraph 1 of this Article shall not apply to:  
The processing which is occasional, does not include, on a large scale, processing of special categories of data as referred to in Article 9 paragraph 1 or processing of personal data relating to criminal convictions and offenses referred to in Article 10, and is unlikely to result in a risk to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes of the processing.  
This means that when we do processing that is occasional (which it will likely not be), does not include special categories of data referred in article 9 paragraph 1, criminal convictions and offenses referred in article 10 and is unlikely to result in risks to the rights and freedom of people. But the nature, context, scope, and purposes of the processing needs to be taken into account.

Paragraph 3 is about where the representative needs to be established in relation to the data subject.  
This paragraph relies on knowing the location of the data subject(s) thus you could reason that you need to know where they live but as this information can be unneeded, we can't request it unless it's for this paragraph and other articles in this regulation to fulfill our duties to comply with the GDPR and other legal instances.

Paragraph 4 is about that the representative needs to be mandated by the controller or processor to be addressed in addition to or instead of the controller or the processor by, in particular, supervisory authorities and data subjects, on all issues related to processing, for the purposes of ensuring compliance with this Regulation.  
As this is about the representative alone, I will not recommend anything other than that the representative shall act on all issues related to processing, for the purposes of ensuring compliance with this Regulation.  

Paragraph 5 The designation of a representative by the controller or processor shall be without prejudice to legal actions which could be initiated against the controller or the processor themselves.  
For this I recommend having a representative from an outside source and not one that is part of the platform that the controller or processor manages.

Suitable Recitals: 80

## Article 28 Processor

In this article the controller should make sure that the processors that they use ensure GDPR compliance. Processors need controller’s permission to subcontract. Processing must be governed by a legal contract or other legal act under Union or Member State law. Processors must follow controller’s instructions, ensure confidentiality, assist the controller, and provide necessary compliance information.

Thus, if the DVerse project or the host/owner of such instance is a processor they need to follow this article closely. When they are on the Controller side, they mainly need to find reliable processors.

Suitable Recitals: 81

## Article 29 Processing under the authority of the controller or processor

Paragraph 1 The processor and any person acting under the authority of the controller or of the processor, who has access to personal data, shall not process those data except on instructions from the controller, unless required to do so by Union or Member State law.

You could say that the bots in the system are the processor but that is not completely right because this is not a natural or legal person, public authority, agency, or other body which processes personal data on behalf of the controller. Thus, they can do it but behind these bots is a person or body which processes personal data on behalf of the controller.  
So based on this only the instructions made for the entire DVerse project should apply to the processing of personal data.

Suitable Recitals: -

## Article 30 Records of processing activities

Paragraph 1 each controller and, where applicable, the controller’s representative, shall maintain a record of processing activities under its responsibility. That record shall contain all of the following information:

1. the name and contact details of the controller and, where applicable, the joint controller, the controller’s representative, and the data protection officer.
1. the purposes of the processing.
1. a description of the categories of data subjects and of the categories of personal data.
1. the categories of recipients to whom the personal data have been or will be disclosed including recipients in third countries or international organizations.
1. where applicable, transfers of personal data to a third country or an international organization, including the identification of that third country or international organization and, in the case of transfers referred to in the second subparagraph of Article 49 paragraph 1, the documentation of suitable safeguards.
1. where possible, the envisaged time limits for erasure of the different categories of data.
1. where possible, a general description of the technical and organizational security measures referred to in Article 32 paragraph 1.

I recommend automating some parts of this like the first point which can be documented in a file which can be used in the entire website if it needs to be brought up. Furthermore, I think that the first few are just groundwork to have a reliable instance of the DVerse project.

Paragraph 2 Each processor and, where applicable, the processor’s representative shall maintain a record of all categories of processing activities carried out on behalf of a controller, containing:

1. the name and contact details of the processor or processors and of each controller on behalf of which the processor is acting, and, where applicable, of the controller’s or the processor’s representative, and the data protection officer.
1. the categories of processing carried out on behalf of each controller.
1. where applicable, transfers of personal data to a third country or an international organization, including the identification of that third country or international organization and, in the case of transfers referred to in the second subparagraph of Article 49 paragraph 1, the documentation of suitable safeguards.
1. where possible, a general description of the technical and organizational security measures referred to in Article 32 paragraph 1.

Well for this paragraph there are some similarities between the first paragraph of this article. Furthermore, when a processor is chosen the first point of this paragraph should be written down. The second point you can look as the second of the first paragraph, but it can be different.

Paragraph 3 The records referred to in paragraphs 1 and 2 shall be in writing, including in electronic form.  
This means that you write it down or make a digital document that does regarding paragraph 1 and 2.

Paragraph 4 The controller or the processor and, where applicable, the controller’s or the processor’s representative, shall make the record available to the supervisory authority on request.
If a supervisory authority requests these forms/documents, then I recommend fulfilling this as soon as possible by having the contacted person be responsible for it or the general representative that is chosen.

Paragraph 5  The obligations referred to in paragraphs 1 and 2 shall not apply to an enterprise or an organization employing fewer than 250 persons unless the processing it carries out is likely to result in a risk to the rights and freedoms of data subjects, the processing is not occasional, or the processing includes special categories of data as referred to in Article 9 paragraph 1 or personal data relating to criminal convictions and offenses referred to in Article 10.

Well now with this information most of the instances of this project will not need to do this. Unless of course the data is in risk of infringing on the rights and freedom of data subjects, processing is not occasional, processing includes special categories of data as referred to in Article 9 paragraph 1 or personal data relating to criminal convictions and offenses referred to in Article 10. I could say that with how the Fediverse is that it can risky that not every server or instance will hold to the GDPR. Then for special categories I do not know if any questions will come to this. In larger communities the processing will likely not be occasional. Related to criminal convictions and offenses is up to the owner/host of the instance of the DVerse project.

Suitable Recitals: 13, 82

## Article 31 Cooperation with the supervisory authority

Paragraph 1 The controller and the processor and, where applicable, their representatives, shall cooperate, on request, with the supervisory authority in the performance of its tasks.

I recommend to just do what the supervisory authority asks you to-do further nothing more. Although it needs to be checked if it’s a supervisory authority to decrease chance of data leaks.

Suitable Recitals: 82

## Article 32 Security of processing

Paragraph 1 Taking into account the state of the art, the costs of implementation and the nature, scope, context, and purposes of processing as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk:

1. the pseudonymization and encryption of personal data.
1. the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services.
1. the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident.
1. a process for regularly testing, assessing, and evaluating the effectiveness of technical and organizational measures for ensuring the security of the processing.

For this I recommend integrating the first point of this paragraph at least. Furthermore, the second point can't be sure that it will be kept as likely everybody can create their own server/instance of the DVerse project. The third point is something that can happen but I'm not sure how we check the technical incident such as question answer not returned, or account was deleted while the data subject this not wanted.  
The fourth point is something that needs to be in the repository of the project where you can see on what it tests, how it tests and what measures were taken.

Paragraph 2 In assessing the appropriate level of security account shall be taken in particular of the risks that are presented by processing, in particular from accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to personal data transmitted, stored, or otherwise processed.

I recommend that you take into account that this project is part of the Fediverse or will be. Thus, not everything can be guaranteed such as having the same level as protection, handling of data and having experience with the law regarding data. So, with that you can find the appropriate level of security that will be the same across with some higher if the owner/host of the server wishes.

Paragraph 3 Adherence to an approved code of conduct as referred to in Article 40 or an approved certification mechanism as referred to in Article 42 may be used as an element by which to demonstrate compliance with the requirements set out in paragraph 1 of this Article.

With this paragraph I recommend making a code of conduct if you wish to follow this paragraph. Or when you wish to possess a certification.

Paragraph 4 The controller and processor shall take steps to ensure that any natural person acting under the authority of the controller or the processor who has access to personal data does not process them except on instructions from the controller unless he or she is required to do so by Union or Member State law.

For this I recommend that personal data may only be accessed by individuals that are accepted by the controller or processor. As such saving it to a database may only happen if that bot is under control of the host/owner of the DVerse instance. Furthermore, as the DVerse project gives the freedom to the individuals to make their own bots there needs to be control on when there are problems such as an unknown bot in that is connected or has access to the personal data.

Suitable Recitals: 75, 76, 77, 78, 79, 83

## Article 33 Notification of a personal data breach to the supervisory authority

This article in short describes when a data breach happens what you need to do to notify the supervisory authority. Both the controller and processor need to do this. In paragraph 3 it describes what the contents needs to be regarding the notification. In paragraph 5 it says that the controller needs to make a document on any personal data breaches, comprising the facts relating to the personal data breach, its effects and the remedial action taken.

In short, I recommend that you notify immediately the supervisory authority with the contents that is specified in paragraph 3.

Suitable Recitals: 85, 87, 88

## Article 34 Communication of a personal data breach to the data subject

Paragraph 1 When the personal data breach is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall communicate the personal data breach to the data subject without undue delay.  
I recommend that when a data breach happens that you immediately communicate to the data subject that their personal data has been leaked.

Paragraph 2 The communication to the data subject referred to in paragraph 1 of this Article shall describe in clear and plain language the nature of the personal data breach and contain at least the information and measures referred to in points (b), (c) and (d) of Article 33 paragraph 3.  
For this I recommend keeping the writing to the level of B1 of the [global Common Reference levels](https://www.coe.int/en/web/common-european-framework-reference-languages/table-1-cefr-3.3-common-reference-levels-global-scale) as the max and when possible have it be in their specified language.

Paragraph 3 the communication to the data subject referred to in paragraph 1 shall not be required if any of the following conditions are met:

1. the controller has implemented appropriate technical and organizational protection measures, and those measures were applied to the personal data affected by the personal data breach, particularly those that render the personal data unintelligible to any person who is not authorized to access it, such as encryption.
1. the controller has taken subsequent measures which ensure that the high risk to the rights and freedoms of data subjects referred to in paragraph 1 is no longer likely to materialize.
1. it would involve disproportionate effort. In such a case, there shall instead be a public communication or similar measure whereby the data subjects are informed in an equally effective manner.

For this paragraph I recommend when applicable you do encryption to maximize the security standard. Send only the necessary data and doing this over a secure connection. If something will take a lot of effort for something not that important then I recommend that it will be communicated to the affected parties that this cannot be done as it's disproportionate to the effort needed to add this.

Paragraph 4 If the controller has not already communicated the personal data breach to the data subject, the supervisory authority, having considered the likelihood of the personal data breach resulting in a high risk, may require it to do so or may decide that any of the conditions referred to in paragraph 3 are met.  
I recommend following the supervisory authority and communicate what they tell you to do.

Suitable Recitals: 86, 87, 88

## Article 35 Data protection impact assessment

In this article I says what the rules are about when to do an impact assessment. With whom you need to communicate to follow the regulation and what the assessment contents need to be.

Suitable Recitals: 75, 84, 89, 90, 91, 92, 93

## Article 36 Prior consultation

Paragraph 1 The controller shall consult the supervisory authority prior to processing where a data protection impact assessment under Article 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk.  

In relation when an impact assessment is high risk then the supervisory authority needs to be consulted or another assessment needs to be made that will prevent this high risk that were created by the first assessment.

Paragraph 2 That if the supervisory authority finds that the controller has not taken enough measures, the supervisory authority shall, within period of up to eight weeks of receipt of the request for consultation, provide written advice to the controller and, where applicable to the processor, and may use any of its powers referred to in Article 58.  
That period may be extended by six weeks, taking into account the complexity of the intended processing.  
The supervisory authority shall inform the controller and, where applicable, the processor, of any such extension within one month of receipt of the request for consultation together with the reasons for the delay.  
Those periods may be suspended until the supervisory authority has obtained information it has requested for the purposes of the consultation.  

So, I recommend that as fast as possible that you fulfill the request of the supervisory authority and check when it takes longer than 8 weeks why this has taken so long if no further communication was brought up.

Paragraph 3 is about what you need to give to the supervisory authority as a controller. As such I recommend that you check this paragraph for yourself and follow it. The most important things regarding the DVerse platform that need to be given are the purposes and means of the intended processing and the measures and safeguards provided to protect the rights and freedoms of data subjects pursuant to the GDPR.

Paragraph 4 is for the member states and has nothing to do with the DVerse Project so will be skipped.

Paragraph 5 is that with member state law may require controllers to consult with, and obtain prior authorization from, the supervisory authority.  
Thus, I can only recommend that you follow the member state law also which cannot be included in the basis of the DVerse project.

Suitable Recitals: 94, 95, 96

## Article 37 Designation of the data protection officer

This article is about how to designate a data protection officer and when it needs to be designated.  
The important paragraphs for this project are 1, 2, 5, 6 and 7.

Suitable Recitals: 97

## Article 38 Position of the data protection officer

This article is about how the controller and processor need to handle the data protection officer. That the data subjects can contact this officer regarding all issues related to processing of their personal data and to the exercise of their rights under this Regulation.  
Furthermore, what the data protection officer may or may not do.

I recommend that as the controller or the processor ensure that the data protection officer is involved, properly and in timely manner with regards to protection of personal data.

Suitable Recitals: 97

## Article 39 Tasks of the data protection officer

I will skip this article for the reason it's only necessary for the data protection officer.  
As they are tasks that need to be done, I cannot recommend something else.

Suitable Recitals: 97

## Article 40 Codes of conduct

This article is about The Member States, the supervisory authorities, the Board, and the Commission. You could also add Associations and other bodies representing categories of controllers or processors. But this has nothing to do with the DVerse project.

Suitable Recitals: 98, 99

## Article 41 Monitoring of approved codes of conduct

This article is about how the competent supervisory authority under Articles 57 and 58, the monitoring of compliance with a code of conduct pursuant to Article 40 may be carried out by a body which has an appropriate level of expertise in relation to the subject-matter of the code and is accredited for that purpose by the competent supervisory authority. With this they check if the codes of conduct are being followed.

Suitable Recitals: -

## Article 42 Certification

This article describes how certification is handled for compliance with the GDPR.

Suitable Recitals: 100

## Article 43 Certification bodies

The article describes what the Certification bodies are and what they are supposed to-do.

Suitable Recitals: -

## Article 44 General principle for transfers

Paragraph 1 Any transfer of personal data which are undergoing processing or are intended for processing after transfer to a third country or to an international organization shall take place only if, subject to the other provisions of this Regulation, the conditions laid down in this Chapter are complied with by the controller and processor, including for onward transfers of personal data from the third country or an international organization to another third country or to another international organization. All provisions in this Chapter shall be applied in order to ensure that the level of protection of natural persons guaranteed by this Regulation is not undermined.

So, in short, we need to keep the same level of protection of natural persons. When it’s transferred to a third country or to an international organization, we need to make sure that the conditions laid down in this Chapter (Transfers of personal data to third countries or international organizations) are complied with by the controller and processor, including for onward transfers.

Suitable Recitals: 101, 102

## Article 45 Transfers on the basis of an adequacy decision

This article is about when the Commission has decided that a third country, a territory or one or more specified sectors within that third country, or the international organization in question ensures an adequate level of protection. The transfer can go through. Further paragraphs in this article relate more to the Commission and how they specify what the level of security needs to be, how it can monitor the level of protection and other similar things.

Thus, for this I recommend allowing that sensitive information will only be transferred to a third country, a territory or one or more specified sectors within that third country, or an international organization that ensures an adequate level of protection. Provided by the commission.

Suitable Recitals: 103, 104, 105, 106, 107

## Article 46 Transfers subject to appropriate safeguards

Paragraph 1 In the absence of a decision pursuant to Article 45 paragraph 3, a controller or processor may transfer personal data to a third country or an international organization only if the controller or processor has provided appropriate safeguards, and on condition that enforceable data subject rights and effective legal remedies for data subjects are available.  
I recommend that the appropriate safeguards need to be made and make it so the data subjects rights can be enforced with effective legal remedies.

Paragraph 2 The appropriate safeguards referred to in paragraph 1 may be provided for, without requiring any specific authorization from a supervisory authority, by:

1. a legally binding and enforceable instrument between public authorities or bodies.
1. binding corporate rules in accordance with Article 47.
1. standard data protection clauses adopted by the Commission in accordance with the examination procedure referred to in Article 93 paragraph 2.
1. standard data protection clauses adopted by a supervisory authority and approved by the Commission pursuant to the examination procedure referred to in Article 93 paragraph 2.
1. an approved code of conduct pursuant to Article 40 together with binding and enforceable commitments of the controller or processor in the third country to apply the appropriate safeguards, including as regards data subjects’ rights.
1. an approved certification mechanism pursuant to Article 42 together with binding and enforceable commitments of the controller or processor in the third country to apply the appropriate safeguards, including as regards data subjects’ rights.

I recommend that you make a contract if the Commission finds that it has not the appropriate level of security or is under investigation if it has the appropriate level of security. Furthermore, I suggest implementing all standard data protections.

Paragraph 3 Subject to the authorization from the competent supervisory authority, the appropriate safeguards referred to in paragraph 1 may also be provided for, in particular, by:

1. contractual clauses between the controller or processor and the controller, processor, or the recipient of the personal data in the third country or international organization; or
1. provisions to be inserted into administrative arrangements between public authorities or bodies which include enforceable and effective data subject rights.

This will mean that the points described in this paragraph can be used to fulfill the obligation to have appropriate safeguards.

Paragraph 4 The supervisory authority shall apply the consistency mechanism referred to in Article 63 in the cases referred to in paragraph 3 of this Article.  
This does not concern the DVerse project and thus no recommendations can be made.

Paragraph 5 is about how Authorizations under Article 26(2) of Directive 95/46/EC remain valid until changed if needed. Decisions under Article 26 paragraph 4 of the same directive stay in force until modified if necessary.
As this has no action points that the DVerse can do there will not be any recommendations.

Suitable Recitals: 108, 109

## Article 47 Binding corporate rules

This article will be skipped since the DVerse project will not be subject to corporate rules as it’s not a corporation but individuals that will have an instance of the project with the DVerse rules and possible additional rules.  
When a host/owner is a corporation then they will need to follow this.

Suitable Recitals: 110

## Article 48 Transfers or disclosures not authorized by Union law

Paragraph 1 Any judgment of a court or tribunal and any decision of an administrative authority of a third country requiring a controller or processor to transfer or disclose personal data may only be recognized or enforceable in any manner if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union or a Member State, without prejudice to other grounds for transfer pursuant to this Chapter.

So based on the international agreement, such as a mutual legal assistance treaty, that's in force between the requesting third country and the Union or a Member State.  
As I am not fully versed into the legal terms, I believe that because there will be multiple instance of the same project but are running in different countries/county's when a person in Europe is a member of the platform but talked with a host on the American side when the administrative authority (of America) requests info from this person it needs to follow the international agreement.  
But when it's an American member talking with a host on the American side and the administrative authority (of America) requests info it isn't hindered by international agreements.

Suitable Recitals: 115

## Article 49 Derogations for specific situations

It allows data transfer to non-EU countries in specific situations like explicit consent, contract necessity, public interest, legal claims, vital interests, and public registers. If none apply, limited non-repetitive transfer for compelling legitimate interests is allowed. The controller must inform the supervisory authority and the data subject.

So, depending on the situation we can transfer information to non-EU countries but that depends on the level of security, consent from the data subject and other things as contracts, legal claims, and vital interest. Thus, as such I recommend limiting the transfers to non-EU countries and inform the data subject if it does go outside this scope (handled in EU countries).

Suitable Recitals: 111, 112, 113, 114, 115

## The other articles

As the other articles has no clear impact on implementation details, is for supervisory authorities, European data protection board, or Remedies, liability, and penalties. So, I have decided to skip it in this document a person can check this on their own and come to their own conclusions. If the person who reads this finds it that it needs to be considered, then based on the reason it will be provided in this document or a separate one.

## Conclusion

In short, I recommend that you look at articles 12 through 23 as this concerns the rights of the data subjects in our applications and that you look at my recommendations and implement them if possible.  
The following articles are also high on my priority of having it for this project: 5, 6, 7, 8, 25, 26 (as it will be part of the Fediverse), 31, 32, 33, 34 and 44.  
I have chosen these by use of what the Fediverse is and what situations are important for it or will happen. Furthermore, the first 4 specified articles are all about how we can lawfully get personal data and need to specify why we need it. As for 32 to 34 it's mostly about security by design and when we get a data breach, as this likely to happen when giving individuals the power to make their own bots/services. What needs to happen.

I also want to recommend that you at least skim through article 4 as to get a better idea of what the definitions are for manners as controller and processor which I repeatedly use in this document.  
For the action points that I wish to see in the DVerse project is that a terms of service and privacy statement will be created or basis for it.  So, the data subject knows their rights, how they can exercise their rights, what happens with their data and what we save.  
In the database or via communication I wish that personal data with encryption and anonymization will be used but alas this is an open source project so a part of this will fall through but we can make it so the host/owner of the DVerse instance first needs to generate the encryption keys that will be used for their instance so it will take a bit longer to crack the data inside of that instance. For anonymization the DVerse project can have a basis and that the instance host/owner needs to develop it further to take the security measure to another level.

I want to finish this document with the following, you can better look through the actual law then my interpretations of it as there can be discrepancies inside of this document. Although I tried to make it as readable as possible with explanations of the paragraphs it's still a wall of text so you can skim through it to find my recommendation and follow it or based on what you skimmed through make your own implementations to follow the paragraph/article.
