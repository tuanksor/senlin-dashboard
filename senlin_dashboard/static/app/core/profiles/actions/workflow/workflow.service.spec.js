/**
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

(function() {
  'use strict';

  describe('horizon.cluster.profiles.actions.workflow', function() {

    var workflow, $scope;

    beforeEach(module('horizon.app.core'));
    beforeEach(module('horizon.framework'));
    beforeEach(module('horizon.cluster.profiles'));

    beforeEach(inject(function($injector, _$rootScope_) {
      $scope = _$rootScope_.$new();
      workflow = $injector.get('horizon.cluster.profiles.actions.workflow');
    }));

    function testInitWorkflow(actionType, title, submitText) {
      var helpUrl;
      helpUrl = 'profile.help.html';

      var config = workflow.init(actionType, title, submitText, helpUrl, $scope);

      expect(config.title).toEqual(title);
      expect(config.submitText).toEqual(submitText);
      expect(config.schema).toBeDefined();
      expect(config.form).toBeDefined();
      return config;
    }

    it('should be create workflow config for create', function() {
      var config = testInitWorkflow('create', 'Create Profile', 'Create');
      expect(config.form[0].items[0].items[1].condition).toEqual(false);
      expect(config.form[0].items[0].items[2].required).toEqual(true);
    });

    it('should be create workflow config for update', function() {
      var config = testInitWorkflow('update', 'Update Profile', 'Update');
      expect(config.form[0].items[0].items[1].condition).toEqual(true);
      expect(config.form[0].items[0].items[2].readonly).toEqual(true);
    });
  });
})();
