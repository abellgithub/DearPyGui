#include "mvVisibleHandler.h"
#include "mvLog.h"
#include "mvItemRegistry.h"
#include "mvPythonExceptions.h"
#include "mvUtilities.h"

namespace Marvel {

	void mvVisibleHandler::InsertParser(std::map<std::string, mvPythonParser>* parsers)
	{

		mvPythonParser parser(mvPyDataType::UUID, "Adds a handler which runs a given callback when the specified item is visible.", { "Events", "Widgets" });
		mvAppItem::AddCommonArgs(parser, (CommonParserArgs)(
			MV_PARSER_ARG_ID |
			MV_PARSER_ARG_SHOW |
			MV_PARSER_ARG_PARENT |
			MV_PARSER_ARG_CALLBACK)
		);

		parser.finalize();

		parsers->insert({ s_command, parser });
	}

	mvVisibleHandler::mvVisibleHandler(mvUUID uuid)
		:
		mvAppItem(uuid)
	{

	}

	void mvVisibleHandler::draw(ImDrawList* drawlist, float x, float y)
	{

		bool run = false;
		if (_parentPtr->getType() == mvAppItemType::mvWindowAppItem)
		{
			if (_parentPtr->isShown())
				run = true;
		}
		else if (ImGui::IsItemVisible())
			run = true;

		if (run)
		{
			mvApp::GetApp()->getCallbackRegistry().submitCallback([=]()
				{
					if (_alias.empty())
						mvApp::GetApp()->getCallbackRegistry().runCallback(getCallback(false), _uuid, GetPyNone(), _user_data);
					else
						mvApp::GetApp()->getCallbackRegistry().runCallback(getCallback(false), _alias, GetPyNone(), _user_data);
				});
		}
	}
}