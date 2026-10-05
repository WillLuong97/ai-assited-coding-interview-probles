'''
 * 
 * Given a list of rules in  rules.txt, where the first 3 strings are the host,method and path that leads to the destination, which is the last string in the line 
 * You are given a list of string in requests.txt, that would contains the host,method , path
 * 
 * Desigin a path router that can return the exact destination matching the rules in the rule list. 
 * 
 * A rule is matched if the below requirements are sastisfied 
 * 1. If "*" is found, then we will assume that whatever it is in the request string can go through, i.e, a wildcard 
 * 2. For the path, if "/" is present in the rule, then whatever it is in the request string can go through
 * 3. If 2 or more matches are found, then prioritize the ones that is closest to the rule. For example, if the request host is api.inference.com and we have 2 choices between "*" and "api.inference.com", we will 
 * 
 * 
 * Example: 
 * select the ones that fully write out the string "api.inference.com"
 * rules_list = {
        {"*", "*", "/", "default-cluster"},
        {"api.com", "*", "/api", "default-api-cluster"},
        {"api.inference.com", "POST", "/api/server/inference", "inference-cluster"},
        {"api.inference.com", "POST", "/api/server/", "inference-cluster"}
        {"api.gpu.com", "GET", "/api/gpu", "gpu-cluster"},
        {"api.workflow.com", "POST", "/workflow", "workflow-cluster"},
    };
 * requests = ["api.inference.com", "POST", "/api/server/inference"],
 * result = "inference-cluster"
 * 
 * for all matching rules:
 * - We will give out a score of 1 for a full string match, i.e, "api.inference.com" == "api.inference.com" or /api/server/inference == /api/server/inference
 * - We will give out a score of 0.5 for a partial string match, i.e, "/api/server/" vs "/api/server/inference", however, during the matching, if we encounter multiple path that are not fully equal to the request path but they are clost to it, then we will award the 0.5 point to 
 * the rule that has a longer string, and closer to the request, for example, when comparing the request path to be "/api/server/inference" against "/api" and "/api/server", we will award the point to "/api/server" instead of "/api"
 * 
 * 
 '''

from router import Router

def main(): 
    print("Starting path router...")
    with open("rules.txt",  encoding="utf-8") as ruleFile: 
        rules = ruleFile.read().splitlines()
    
    with open("rules.txt",  encoding="utf-8") as requestFile: 
        requests = requestFile.read().splitlines()

    router = Router(rules)
    destination = router.destination(rules, requests)


    assert destination == "inference-cluster"


