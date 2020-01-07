import unittest

import filter

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.mock_posts = [
            {
                'id': 'id1',
                'title': 't1',
                'company': 'c1'
            },
            {
                'id': 'id2',
                'title': 't2',
                'company': 'c2'
            },
            {
                'id': 'id3',
                'title': 't3',
                'company': 'c3'
            },
            {
                'id': 'id4',
                'title': 't4',        
                'company': 'c4'
            }
        ]
    
    def tearDown(self):
        pass

    def get_mock_history_path(self, number):
        return './mock_data/indeed_ids_history_t{0}.csv'.format(number)

    def get_mock_exclusion_path(self, number):
        return './mock_data/exclude_t{0}.csv'.format(number)


class TestExcludeSeen(TestFilters):    

    def test_no_post_excluded_from_empty_history(self):
        """
        Should not filter out any job posts when history of seen post IDs is empty.
        """

        expected = self.mock_posts
        post_list = filter.exclude_seen(self.mock_posts, self.get_mock_history_path(1))
        self.assertEqual(post_list, expected)

    def test_posts_are_excluded(self):
        """
        Should filter out job posts with job IDs that are recorded in history.
        """

        expected = [
            {
                'id': 'id2',
                'title': 't2',
                'company': 'c2'
            },
            {
                'id': 'id4',
                'title': 't4',
                'company': 'c4'
            }
        ]
        post_list = filter.exclude_seen(self.mock_posts, self.get_mock_history_path(2))
        self.assertEqual(post_list, expected)


class TestExcludeCompanies(TestFilters):    

    def test_no_post_excluded_when_no_company_is_listed(self):
        """
        Should not filter out any job posts when there is no company name in the exclusion CSV file.
        """

        expected = self.mock_posts
        post_list = filter.exclude_companies(self.mock_posts, self.get_mock_exclusion_path(3))
        self.assertEqual(post_list, expected)


    def test_posts_are_excluded_when_company_is_listed(self):
        """
        Should not filter out any job posts when there is no company name in the exclusion CSV file.
        """

        expected = [
            {
                'id': 'id2',
                'title': 't2',
                'company': 'c2'
            },
            {
                'id': 'id4',
                'title': 't4',
                'company': 'c4'
            }
        ]
        post_list = filter.exclude_companies(self.mock_posts, self.get_mock_exclusion_path(4))
        self.assertEqual(post_list, expected)




if __name__ == '__main__':
    unittest.main()