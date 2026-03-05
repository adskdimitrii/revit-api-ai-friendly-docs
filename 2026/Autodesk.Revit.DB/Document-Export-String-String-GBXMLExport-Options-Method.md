# Document Export(String, String, GBXMLExport Options) Method

Source: https://www.revitapidocs.com/2026/adf1b78e-dcab-7b46-80fa-a470f0fd848b.htm

---

| Document Export(String, String, GBXMLExport Options) Method |
| --- |

Export the model in gbXML (green\-building) format. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool Export(
	string folder,
	string name,
	GBXMLExportOptions options
)
```

```
Public Function Export ( 
	folder As String,
	name As String,
	options As GBXMLExportOptions
) As Boolean
```

```
public:
bool Export(
	String^ folder, 
	String^ name, 
	GBXMLExportOptions^ options
)
```

```
member Export : 
        folder : string * 
        name : string * 
        options : GBXMLExportOptions -> bool 
```

#### Parameters

folder String
:   Indicates the path of a folder where to export the gbXML file.

name String
:   Indicates the name of the gbXML file to export. If it doesn't end with ".xml", extension ".xml" will be added automatically. The name cannot contain any of the following characters: \\/:\*?"\<\>\|. Empty name is not acceptable.

options [GBXMLExportOptions](GBXMLExport-Options-Class.md)
:   Options which control the contents of the export.

#### Return Value

Boolean 
True if successful, otherwise False. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The path is not valid for exporting gbXML files.  \-or\-  The name is empty or not valid for exporting gbXML files.  \-or\-  There is no main EnergyAnalysisDetailModel in the document, or the current main EnergyAnalysisDetailModel is not compatible with the option set in the GBXMLExportOptions. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Exporting is not allowed in the current application mode.  \-or\-  Export is temporarily disabled. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This export operation will operate on the main EnergyAnalysisDetailModel in the document, if it exists (see EnergyAnalysisDetailModel.GetMainEnergyAnalysisDetailModel()).
 If it does not exist, or if the requested ExportEnergyModelType does not match the type of the main EnergyAnalysisDetailModel, this function will fail.
 If you need to export a model with different settings or type than the current main energy model in the document, you should delete the current main energy model, update the EnergyAnalysisSettings, and regenerate the energy model.
 This method should be called from a transaction. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
