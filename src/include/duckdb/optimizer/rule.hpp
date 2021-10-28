//===----------------------------------------------------------------------===//
//                         DuckDB
//
// duckdb/optimizer/rule.hpp
//
//
//===----------------------------------------------------------------------===//

#pragma once

#include "duckdb/optimizer/matcher/expression_matcher.hpp"
#include "duckdb/optimizer/matcher/logical_operator_matcher.hpp"

namespace duckdb {
class ExpressionRewriter;

class Rule {
public:
	explicit Rule(ExpressionRewriter &rewriter) : rewriter(rewriter) {
	}
	virtual ~Rule() {
	}

	//! The expression rewriter this rule belongs to
	ExpressionRewriter &rewriter;
	//! The root
	unique_ptr<LogicalOperatorMatcher> logical_root;
	//! The expression matcher of the rule
	unique_ptr<ExpressionMatcher> root;
	//! If the rule requires the expression to be root
	bool requires_root = false;

	virtual unique_ptr<Expression> Apply(LogicalOperator &op, vector<Expression *> &bindings, bool &fixed_point,
	                                     bool is_root) = 0;
};

} // namespace duckdb
