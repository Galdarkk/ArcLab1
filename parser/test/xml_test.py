import parser.parse_xml as xml
import os


def parse_links_test():
    test_res = '\tucityt.parser.parse_xml.parse_links test'
    path = os.path.join(os.getcwd(), 'test_data', 'links')
    links = xml.parse_links(path)
    expected_links = ['http://www.feedforall.com/sample.xml']
    try:
        assert links == expected_links
        return '✔ passed' + test_res
    except AssertionError:
        return '✘ not passed' + test_res


def parse_xmls_test():
    test_res = '\tucityt.parser.parse_xml.parse_xmls test'
    xml_to_parse = '<?xml version="1.0" encoding="windows-1252"?>\r\n<rss version="2.0">\r\n  <channel>\r\n    <title>FeedForAll Sample Feed</title>\r\n    <description>RSS is a fascinating technology. The uses for RSS are expanding daily. Take a closer look at how various industries are using the benefits of RSS in their businesses.</description>\r\n    <link>http://www.feedforall.com/industry-solutions.htm</link>\r\n    <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n    <copyright>Copyright 2004 NotePage, Inc.</copyright>\r\n    <docs>http://blogs.law.harvard.edu/tech/rss</docs>\r\n    <language>en-us</language>\r\n    <lastBuildDate>Tue, 19 Oct 2004 13:39:14 -0400</lastBuildDate>\r\n    <managingEditor>marketing@feedforall.com</managingEditor>\r\n    <pubDate>Tue, 19 Oct 2004 13:38:55 -0400</pubDate>\r\n    <webMaster>webmaster@feedforall.com</webMaster>\r\n    <generator>FeedForAll Beta1 (0.0.1.8)</generator>\r\n    <image>\r\n      <url>http://www.feedforall.com/ffalogo48x48.gif</url>\r\n      <title>FeedForAll Sample Feed</title>\r\n      <link>http://www.feedforall.com/industry-solutions.htm</link>\r\n      <description>FeedForAll Sample Feed</description>\r\n      <width>48</width>\r\n      <height>48</height>\r\n    </image>\r\n    <item>\r\n      <title>RSS Solutions for Restaurants</title>\r\n      <description>&lt;b&gt;FeedForAll &lt;/b&gt;helps Restaurant&apos;s communicate with customers. Let your customers know the latest specials or events.&lt;br&gt;\r\n&lt;br&gt;\r\nRSS feed uses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#FF0000&quot;&gt;Daily Specials &lt;br&gt;\r\nEntertainment &lt;br&gt;\r\nCalendar of Events &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/restaurant.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:11 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Schools and Colleges</title>\r\n      <description>FeedForAll helps Educational Institutions communicate with students about school wide activities, events, and schedules.&lt;br&gt;\r\n&lt;br&gt;\r\nRSS feed uses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Homework Assignments &lt;br&gt;\r\nSchool Cancellations &lt;br&gt;\r\nCalendar of Events &lt;br&gt;\r\nSports Scores &lt;br&gt;\r\nClubs/Organization Meetings &lt;br&gt;\r\nLunches Menus &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/schools.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:09 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Computer Service Companies</title>\r\n      <description>FeedForAll helps Computer Service Companies communicate with clients about cyber security and related issues. &lt;br&gt;\r\n&lt;br&gt;\r\nUses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Cyber Security Alerts &lt;br&gt;\r\nSpecials&lt;br&gt;\r\nJob Postings &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/computer-service.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:07 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Governments</title>\r\n      <description>FeedForAll helps Governments communicate with the general public about positions on various issues, and keep the community aware of changes in important legislative issues. &lt;b&gt;&lt;i&gt;&lt;br&gt;\r\n&lt;/b&gt;&lt;/i&gt;&lt;br&gt;\r\nRSS uses Include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#00FF00&quot;&gt;Legislative Calendar&lt;br&gt;\r\nVotes&lt;br&gt;\r\nBulletins&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/government.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:05 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Politicians</title>\r\n      <description>FeedForAll helps Politicians communicate with the general public about positions on various issues, and keep the community notified of their schedule. &lt;br&gt;\r\n&lt;br&gt;\r\nUses Include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#FF0000&quot;&gt;Blogs&lt;br&gt;\r\nSpeaking Engagements &lt;br&gt;\r\nStatements&lt;br&gt;\r\n &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/politics.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:03 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Meteorologists</title>\r\n      <description>FeedForAll helps Meteorologists communicate with the general public about storm warnings and weather alerts, in specific regions. Using RSS meteorologists are able to quickly disseminate urgent and life threatening weather warnings. &lt;br&gt;\r\n&lt;br&gt;\r\nUses Include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Weather Alerts&lt;br&gt;\r\nPlotting Storms&lt;br&gt;\r\nSchool Cancellations &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/weather.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:01 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Realtors &amp; Real Estate Firms</title>\r\n      <description>FeedForAll helps Realtors and Real Estate companies communicate with clients informing them of newly available properties, and open house announcements. RSS helps to reach a targeted audience and spread the word in an inexpensive, professional manner. &lt;font color=&quot;#0000FF&quot;&gt;&lt;br&gt;\r\n&lt;/font&gt;&lt;br&gt;\r\nFeeds can be used for:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#FF0000&quot;&gt;Open House Dates&lt;br&gt;\r\nNew Properties For Sale&lt;br&gt;\r\nMortgage Rates&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/real-estate.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:08:59 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Banks / Mortgage Companies</title>\r\n      <description>FeedForAll helps &lt;b&gt;Banks, Credit Unions and Mortgage companies&lt;/b&gt; communicate with the general public about rate changes in a prompt and professional manner. &lt;br&gt;\r\n&lt;br&gt;\r\nUses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Mortgage Rates&lt;br&gt;\r\nForeign Exchange Rates &lt;br&gt;\r\nBank Rates&lt;br&gt;\r\nSpecials&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/banks.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:08:57 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Law Enforcement</title>\r\n      <description>&lt;b&gt;FeedForAll&lt;/b&gt; helps Law Enforcement Professionals communicate with the general public and other agencies in a prompt and efficient manner. Using RSS police are able to quickly disseminate urgent and life threatening information. &lt;br&gt;\r\n&lt;br&gt;\r\nUses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Amber Alerts&lt;br&gt;\r\nSex Offender Community Notification &lt;br&gt;\r\nWeather Alerts &lt;br&gt;\r\nScheduling &lt;br&gt;\r\nSecurity Alerts &lt;br&gt;\r\nPolice Report &lt;br&gt;\r\nMeetings&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/law-enforcement.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:08:56 -0400</pubDate>\r\n    </item>\r\n  </channel>\r\n</rss>'
    links = xml.parse_xmls([xml_to_parse])
    expected_links = ['http://www.feedforall.com/restaurant.htm', 'http://www.feedforall.com/schools.htm', 'http://www.feedforall.com/computer-service.htm', 'http://www.feedforall.com/government.htm', 'http://www.feedforall.com/politics.htm', 'http://www.feedforall.com/weather.htm', 'http://www.feedforall.com/real-estate.htm', 'http://www.feedforall.com/banks.htm', 'http://www.feedforall.com/law-enforcement.htm']
    try:
        assert links == expected_links
        return '✔ passed' + test_res
    except AssertionError:
        return '✘ not passed' + test_res


def parse_xml_test():
    test_res = '\tucityt.parser.parse_xml.parse_xml test'
    xml_to_parse = '<?xml version="1.0" encoding="windows-1252"?>\r\n<rss version="2.0">\r\n  <channel>\r\n    <title>FeedForAll Sample Feed</title>\r\n    <description>RSS is a fascinating technology. The uses for RSS are expanding daily. Take a closer look at how various industries are using the benefits of RSS in their businesses.</description>\r\n    <link>http://www.feedforall.com/industry-solutions.htm</link>\r\n    <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n    <copyright>Copyright 2004 NotePage, Inc.</copyright>\r\n    <docs>http://blogs.law.harvard.edu/tech/rss</docs>\r\n    <language>en-us</language>\r\n    <lastBuildDate>Tue, 19 Oct 2004 13:39:14 -0400</lastBuildDate>\r\n    <managingEditor>marketing@feedforall.com</managingEditor>\r\n    <pubDate>Tue, 19 Oct 2004 13:38:55 -0400</pubDate>\r\n    <webMaster>webmaster@feedforall.com</webMaster>\r\n    <generator>FeedForAll Beta1 (0.0.1.8)</generator>\r\n    <image>\r\n      <url>http://www.feedforall.com/ffalogo48x48.gif</url>\r\n      <title>FeedForAll Sample Feed</title>\r\n      <link>http://www.feedforall.com/industry-solutions.htm</link>\r\n      <description>FeedForAll Sample Feed</description>\r\n      <width>48</width>\r\n      <height>48</height>\r\n    </image>\r\n    <item>\r\n      <title>RSS Solutions for Restaurants</title>\r\n      <description>&lt;b&gt;FeedForAll &lt;/b&gt;helps Restaurant&apos;s communicate with customers. Let your customers know the latest specials or events.&lt;br&gt;\r\n&lt;br&gt;\r\nRSS feed uses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#FF0000&quot;&gt;Daily Specials &lt;br&gt;\r\nEntertainment &lt;br&gt;\r\nCalendar of Events &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/restaurant.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:11 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Schools and Colleges</title>\r\n      <description>FeedForAll helps Educational Institutions communicate with students about school wide activities, events, and schedules.&lt;br&gt;\r\n&lt;br&gt;\r\nRSS feed uses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Homework Assignments &lt;br&gt;\r\nSchool Cancellations &lt;br&gt;\r\nCalendar of Events &lt;br&gt;\r\nSports Scores &lt;br&gt;\r\nClubs/Organization Meetings &lt;br&gt;\r\nLunches Menus &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/schools.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:09 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Computer Service Companies</title>\r\n      <description>FeedForAll helps Computer Service Companies communicate with clients about cyber security and related issues. &lt;br&gt;\r\n&lt;br&gt;\r\nUses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Cyber Security Alerts &lt;br&gt;\r\nSpecials&lt;br&gt;\r\nJob Postings &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/computer-service.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:07 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Governments</title>\r\n      <description>FeedForAll helps Governments communicate with the general public about positions on various issues, and keep the community aware of changes in important legislative issues. &lt;b&gt;&lt;i&gt;&lt;br&gt;\r\n&lt;/b&gt;&lt;/i&gt;&lt;br&gt;\r\nRSS uses Include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#00FF00&quot;&gt;Legislative Calendar&lt;br&gt;\r\nVotes&lt;br&gt;\r\nBulletins&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/government.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:05 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Politicians</title>\r\n      <description>FeedForAll helps Politicians communicate with the general public about positions on various issues, and keep the community notified of their schedule. &lt;br&gt;\r\n&lt;br&gt;\r\nUses Include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#FF0000&quot;&gt;Blogs&lt;br&gt;\r\nSpeaking Engagements &lt;br&gt;\r\nStatements&lt;br&gt;\r\n &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/politics.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:03 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Meteorologists</title>\r\n      <description>FeedForAll helps Meteorologists communicate with the general public about storm warnings and weather alerts, in specific regions. Using RSS meteorologists are able to quickly disseminate urgent and life threatening weather warnings. &lt;br&gt;\r\n&lt;br&gt;\r\nUses Include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Weather Alerts&lt;br&gt;\r\nPlotting Storms&lt;br&gt;\r\nSchool Cancellations &lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/weather.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:09:01 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Realtors &amp; Real Estate Firms</title>\r\n      <description>FeedForAll helps Realtors and Real Estate companies communicate with clients informing them of newly available properties, and open house announcements. RSS helps to reach a targeted audience and spread the word in an inexpensive, professional manner. &lt;font color=&quot;#0000FF&quot;&gt;&lt;br&gt;\r\n&lt;/font&gt;&lt;br&gt;\r\nFeeds can be used for:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#FF0000&quot;&gt;Open House Dates&lt;br&gt;\r\nNew Properties For Sale&lt;br&gt;\r\nMortgage Rates&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/real-estate.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:08:59 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Banks / Mortgage Companies</title>\r\n      <description>FeedForAll helps &lt;b&gt;Banks, Credit Unions and Mortgage companies&lt;/b&gt; communicate with the general public about rate changes in a prompt and professional manner. &lt;br&gt;\r\n&lt;br&gt;\r\nUses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Mortgage Rates&lt;br&gt;\r\nForeign Exchange Rates &lt;br&gt;\r\nBank Rates&lt;br&gt;\r\nSpecials&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/banks.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:08:57 -0400</pubDate>\r\n    </item>\r\n    <item>\r\n      <title>RSS Solutions for Law Enforcement</title>\r\n      <description>&lt;b&gt;FeedForAll&lt;/b&gt; helps Law Enforcement Professionals communicate with the general public and other agencies in a prompt and efficient manner. Using RSS police are able to quickly disseminate urgent and life threatening information. &lt;br&gt;\r\n&lt;br&gt;\r\nUses include:&lt;br&gt;\r\n&lt;i&gt;&lt;font color=&quot;#0000FF&quot;&gt;Amber Alerts&lt;br&gt;\r\nSex Offender Community Notification &lt;br&gt;\r\nWeather Alerts &lt;br&gt;\r\nScheduling &lt;br&gt;\r\nSecurity Alerts &lt;br&gt;\r\nPolice Report &lt;br&gt;\r\nMeetings&lt;/i&gt;&lt;/font&gt;</description>\r\n      <link>http://www.feedforall.com/law-enforcement.htm</link>\r\n      <category domain="www.dmoz.com">Computers/Software/Internet/Site Management/Content Management</category>\r\n      <comments>http://www.feedforall.com/forum</comments>\r\n      <pubDate>Tue, 19 Oct 2004 11:08:56 -0400</pubDate>\r\n    </item>\r\n  </channel>\r\n</rss>'
    links = xml.parse_xml(xml_to_parse)
    expected_links = ['http://www.feedforall.com/restaurant.htm', 'http://www.feedforall.com/schools.htm', 'http://www.feedforall.com/computer-service.htm', 'http://www.feedforall.com/government.htm', 'http://www.feedforall.com/politics.htm', 'http://www.feedforall.com/weather.htm', 'http://www.feedforall.com/real-estate.htm', 'http://www.feedforall.com/banks.htm', 'http://www.feedforall.com/law-enforcement.htm']
    try:
        assert links == expected_links
        return '✔ passed' + test_res
    except AssertionError:
        return '✘ not passed' + test_res


def write_words_test():
    test_res = '\tucityt.parser.parse_xml.write_words test'
    dict_to_write = {'test': 0, 'test2': 1}
    xml.write_words(dict_to_write, os.path.join(os.getcwd(), 'test_data', 'test_output'))
    return '✔ passed' + test_res
