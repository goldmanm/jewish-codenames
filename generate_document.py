#!/usr/bin/env python
# coding: utf-8

# In[85]:


import re


# In[86]:


head_matter = """<?xml version="1.0" encoding="UTF-8"?>

<office:document xmlns:officeooo="http://openoffice.org/2009/office" xmlns:anim="urn:oasis:names:tc:opendocument:xmlns:animation:1.0" xmlns:smil="urn:oasis:names:tc:opendocument:xmlns:smil-compatible:1.0" xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rpt="http://openoffice.org/2005/report" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.graphics">
 <office:meta><meta:creation-date>2023-12-04T22:58:36.857575074</meta:creation-date><dc:date>2024-09-08T14:00:55.903735149</dc:date><meta:editing-duration>PT34M5S</meta:editing-duration><meta:editing-cycles>8</meta:editing-cycles><meta:generator>LibreOffice/7.3.7.2$Linux_X86_64 LibreOffice_project/30$Build-2</meta:generator><meta:document-statistic meta:object-count="18"/></office:meta>
 <office:settings>
  <config:config-item-set config:name="ooo:view-settings">
   <config:config-item config:name="VisibleAreaTop" config:type="int">-1467</config:config-item>
   <config:config-item config:name="VisibleAreaLeft" config:type="int">-1960</config:config-item>
   <config:config-item config:name="VisibleAreaWidth" config:type="int">13494</config:config-item>
   <config:config-item config:name="VisibleAreaHeight" config:type="int">10788</config:config-item>
   <config:config-item-map-indexed config:name="Views">
    <config:config-item-map-entry>
     <config:config-item config:name="ViewId" config:type="string">view1</config:config-item>
     <config:config-item config:name="GridIsVisible" config:type="boolean">false</config:config-item>
     <config:config-item config:name="GridIsFront" config:type="boolean">false</config:config-item>
     <config:config-item config:name="IsSnapToGrid" config:type="boolean">true</config:config-item>
     <config:config-item config:name="IsSnapToPageMargins" config:type="boolean">true</config:config-item>
     <config:config-item config:name="IsSnapToSnapLines" config:type="boolean">false</config:config-item>
     <config:config-item config:name="IsSnapToObjectFrame" config:type="boolean">false</config:config-item>
     <config:config-item config:name="IsSnapToObjectPoints" config:type="boolean">false</config:config-item>
     <config:config-item config:name="IsPlusHandlesAlwaysVisible" config:type="boolean">false</config:config-item>
     <config:config-item config:name="IsFrameDragSingles" config:type="boolean">true</config:config-item>
     <config:config-item config:name="EliminatePolyPointLimitAngle" config:type="int">1500</config:config-item>
     <config:config-item config:name="IsEliminatePolyPoints" config:type="boolean">false</config:config-item>
     <config:config-item config:name="VisibleLayers" config:type="base64Binary">Hw==</config:config-item>
     <config:config-item config:name="PrintableLayers" config:type="base64Binary">Hw==</config:config-item>
     <config:config-item config:name="LockedLayers" config:type="base64Binary"/>
     <config:config-item config:name="NoAttribs" config:type="boolean">false</config:config-item>
     <config:config-item config:name="NoColors" config:type="boolean">true</config:config-item>
     <config:config-item config:name="RulerIsVisible" config:type="boolean">true</config:config-item>
     <config:config-item config:name="PageKind" config:type="short">0</config:config-item>
     <config:config-item config:name="SelectedPage" config:type="short">0</config:config-item>
     <config:config-item config:name="IsLayerMode" config:type="boolean">true</config:config-item>
     <config:config-item config:name="IsDoubleClickTextEdit" config:type="boolean">true</config:config-item>
     <config:config-item config:name="IsClickChangeRotation" config:type="boolean">true</config:config-item>
     <config:config-item config:name="SlidesPerRow" config:type="short">4</config:config-item>
     <config:config-item config:name="EditMode" config:type="int">0</config:config-item>
     <config:config-item config:name="VisibleAreaTop" config:type="int">-572</config:config-item>
     <config:config-item config:name="VisibleAreaLeft" config:type="int">324</config:config-item>
     <config:config-item config:name="VisibleAreaWidth" config:type="int">9287</config:config-item>
     <config:config-item config:name="VisibleAreaHeight" config:type="int">7324</config:config-item>
     <config:config-item config:name="GridCoarseWidth" config:type="int">1270</config:config-item>
     <config:config-item config:name="GridCoarseHeight" config:type="int">1270</config:config-item>
     <config:config-item config:name="GridFineWidth" config:type="int">317</config:config-item>
     <config:config-item config:name="GridFineHeight" config:type="int">317</config:config-item>
     <config:config-item config:name="GridSnapWidthXNumerator" config:type="int">1270</config:config-item>
     <config:config-item config:name="GridSnapWidthXDenominator" config:type="int">4</config:config-item>
     <config:config-item config:name="GridSnapWidthYNumerator" config:type="int">1270</config:config-item>
     <config:config-item config:name="GridSnapWidthYDenominator" config:type="int">4</config:config-item>
     <config:config-item config:name="IsAngleSnapEnabled" config:type="boolean">false</config:config-item>
     <config:config-item config:name="SnapAngle" config:type="int">1500</config:config-item>
     <config:config-item config:name="ZoomOnPage" config:type="boolean">false</config:config-item>
     <config:config-item config:name="AnchoredTextOverflowLegacy" config:type="boolean">false</config:config-item>
    </config:config-item-map-entry>
   </config:config-item-map-indexed>
  </config:config-item-set>
  <config:config-item-set config:name="ooo:configuration-settings">
   <config:config-item config:name="ApplyUserData" config:type="boolean">true</config:config-item>
   <config:config-item config:name="BitmapTableURL" config:type="string">$(brandbaseurl)/share/palette%3B$(user)/config/standard.sob</config:config-item>
   <config:config-item config:name="CharacterCompressionType" config:type="short">0</config:config-item>
   <config:config-item config:name="ColorTableURL" config:type="string">$(brandbaseurl)/share/palette%3B$(user)/config/standard.soc</config:config-item>
   <config:config-item config:name="DashTableURL" config:type="string">$(brandbaseurl)/share/palette%3B$(user)/config/standard.sod</config:config-item>
   <config:config-item config:name="DefaultTabStop" config:type="int">1270</config:config-item>
   <config:config-item config:name="EmbedAsianScriptFonts" config:type="boolean">true</config:config-item>
   <config:config-item config:name="EmbedComplexScriptFonts" config:type="boolean">true</config:config-item>
   <config:config-item config:name="EmbedFonts" config:type="boolean">false</config:config-item>
   <config:config-item config:name="EmbedLatinScriptFonts" config:type="boolean">true</config:config-item>
   <config:config-item config:name="EmbedOnlyUsedFonts" config:type="boolean">false</config:config-item>
   <config:config-item-map-indexed config:name="ForbiddenCharacters">
    <config:config-item-map-entry>
     <config:config-item config:name="Language" config:type="string">en</config:config-item>
     <config:config-item config:name="Country" config:type="string">US</config:config-item>
     <config:config-item config:name="Variant" config:type="string"/>
     <config:config-item config:name="BeginLine" config:type="string"/>
     <config:config-item config:name="EndLine" config:type="string"/>
    </config:config-item-map-entry>
   </config:config-item-map-indexed>
   <config:config-item config:name="GradientTableURL" config:type="string">$(brandbaseurl)/share/palette%3B$(user)/config/standard.sog</config:config-item>
   <config:config-item config:name="HatchTableURL" config:type="string">$(brandbaseurl)/share/palette%3B$(user)/config/standard.soh</config:config-item>
   <config:config-item config:name="IsKernAsianPunctuation" config:type="boolean">false</config:config-item>
   <config:config-item config:name="IsPrintBooklet" config:type="boolean">false</config:config-item>
   <config:config-item config:name="IsPrintBookletBack" config:type="boolean">true</config:config-item>
   <config:config-item config:name="IsPrintBookletFront" config:type="boolean">true</config:config-item>
   <config:config-item config:name="IsPrintDate" config:type="boolean">false</config:config-item>
   <config:config-item config:name="IsPrintFitPage" config:type="boolean">false</config:config-item>
   <config:config-item config:name="IsPrintHiddenPages" config:type="boolean">true</config:config-item>
   <config:config-item config:name="IsPrintPageName" config:type="boolean">false</config:config-item>
   <config:config-item config:name="IsPrintTilePage" config:type="boolean">false</config:config-item>
   <config:config-item config:name="IsPrintTime" config:type="boolean">false</config:config-item>
   <config:config-item config:name="LineEndTableURL" config:type="string">$(brandbaseurl)/share/palette%3B$(user)/config/standard.soe</config:config-item>
   <config:config-item config:name="LoadReadonly" config:type="boolean">false</config:config-item>
   <config:config-item config:name="MeasureUnit" config:type="short">2</config:config-item>
   <config:config-item config:name="PageNumberFormat" config:type="int">4</config:config-item>
   <config:config-item config:name="ParagraphSummation" config:type="boolean">false</config:config-item>
   <config:config-item config:name="PrintQuality" config:type="int">0</config:config-item>
   <config:config-item config:name="PrinterIndependentLayout" config:type="string">low-resolution</config:config-item>
   <config:config-item config:name="PrinterName" config:type="string">HL-L2300D-series</config:config-item>
   <config:config-item config:name="PrinterPaperFromSetup" config:type="boolean">false</config:config-item>
   <config:config-item config:name="PrinterSetup" config:type="base64Binary">tAH+/0hMLUwyMzAwRC1zZXJpZXMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQ1VQUzpITC1MMjMwMEQtc2VyaWVzAAAAAAAAAAAAAAAWAAMA1QAAAAAAAAAIAFZUAAAkbQAASm9iRGF0YSAxCnByaW50ZXI9SEwtTDIzMDBELXNlcmllcwpvcmllbnRhdGlvbj1Qb3J0cmFpdApjb3BpZXM9MQpjb2xsYXRlPWZhbHNlCm1hcmdpbmFkanVzdG1lbnQ9MCwwLDAsMApjb2xvcmRlcHRoPTI0CnBzbGV2ZWw9MApwZGZkZXZpY2U9MQpjb2xvcmRldmljZT0wClBQRENvbnRleHREYXRhCkR1cGxleDpOb25lAElucHV0U2xvdDpBdXRvAFBhZ2VTaXplOkxldHRlcgAAEgBDT01QQVRfRFVQTEVYX01PREUPAER1cGxleE1vZGU6Ok9mZg==</config:config-item>
   <config:config-item config:name="SaveThumbnail" config:type="boolean">true</config:config-item>
   <config:config-item config:name="SaveVersionOnClose" config:type="boolean">false</config:config-item>
   <config:config-item config:name="ScaleDenominator" config:type="int">1</config:config-item>
   <config:config-item config:name="ScaleNumerator" config:type="int">1</config:config-item>
   <config:config-item config:name="UpdateFromTemplate" config:type="boolean">true</config:config-item>
  </config:config-item-set>
 </office:settings>
 <office:scripts>
  <office:script script:language="ooo:Basic">
   <ooo:libraries xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink"/>
  </office:script>
 </office:scripts>
 <office:font-face-decls>
  <style:font-face style:name="DejaVu Sans" svg:font-family="&apos;DejaVu Sans&apos;" style:font-family-generic="swiss" style:font-pitch="variable"/>
  <style:font-face style:name="DejaVu Sans1" svg:font-family="&apos;DejaVu Sans&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
  <style:font-face style:name="Liberation Sans" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  <style:font-face style:name="Liberation Sans1" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="swiss" style:font-pitch="variable"/>
  <style:font-face style:name="Liberation Serif" svg:font-family="&apos;Liberation Serif&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  <style:font-face style:name="Lohit Devanagari" svg:font-family="&apos;Lohit Devanagari&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
  <style:font-face style:name="Noto Sans" svg:font-family="&apos;Noto Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  <style:font-face style:name="Noto Sans CJK SC" svg:font-family="&apos;Noto Sans CJK SC&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
 </office:font-face-decls>
 <office:styles>
  <draw:gradient draw:name="Filled" draw:style="linear" draw:start-color="#ffffff" draw:end-color="#cccccc" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/>
  <draw:gradient draw:name="Filled_20_Blue" draw:display-name="Filled Blue" draw:style="linear" draw:start-color="#729fcf" draw:end-color="#355269" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/>
  <draw:gradient draw:name="Filled_20_Green" draw:display-name="Filled Green" draw:style="linear" draw:start-color="#77bc65" draw:end-color="#127622" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/>
  <draw:gradient draw:name="Filled_20_Red" draw:display-name="Filled Red" draw:style="linear" draw:start-color="#ff6d6d" draw:end-color="#c9211e" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/>
  <draw:gradient draw:name="Filled_20_Yellow" draw:display-name="Filled Yellow" draw:style="linear" draw:start-color="#ffde59" draw:end-color="#b47804" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="30deg" draw:border="0%"/>
  <draw:gradient draw:name="Shapes" draw:style="rectangular" draw:cx="50%" draw:cy="50%" draw:start-color="#cccccc" draw:end-color="#ffffff" draw:start-intensity="100%" draw:end-intensity="100%" draw:angle="0deg" draw:border="0%"/>
  <draw:marker draw:name="Arrow" svg:viewBox="0 0 20 30" svg:d="M10 0l-10 30h20z"/>
  <style:default-style style:family="graphic">
   <style:graphic-properties svg:stroke-color="#3465a4" draw:fill-color="#729fcf" fo:wrap-option="no-wrap"/>
   <style:paragraph-properties style:text-autospace="ideograph-alpha" style:punctuation-wrap="simple" style:line-break="strict" style:writing-mode="lr-tb" style:font-independent-line-spacing="false">
    <style:tab-stops/>
   </style:paragraph-properties>
   <style:text-properties style:use-window-font-color="true" loext:opacity="0%" style:font-name="Liberation Serif" fo:font-size="24pt" fo:language="en" fo:country="US" style:font-name-asian="DejaVu Sans1" style:font-size-asian="24pt" style:language-asian="zh" style:country-asian="CN" style:font-name-complex="DejaVu Sans1" style:font-size-complex="24pt" style:language-complex="hi" style:country-complex="IN"/>
  </style:default-style>
  <style:style style:name="standard" style:family="graphic">
   <style:graphic-properties draw:stroke="solid" svg:stroke-width="0cm" svg:stroke-color="#3465a4" draw:marker-start-width="0.2cm" draw:marker-start-center="false" draw:marker-end-width="0.2cm" draw:marker-end-center="false" draw:fill="solid" draw:fill-color="#729fcf" draw:textarea-horizontal-align="justify" fo:padding-top="0.125cm" fo:padding-bottom="0.125cm" fo:padding-left="0.25cm" fo:padding-right="0.25cm" fo:wrap-option="wrap" draw:shadow="hidden" draw:shadow-offset-x="0.2cm" draw:shadow-offset-y="0.2cm" draw:shadow-color="#808080">
    <text:list-style style:name="standard">
     <text:list-level-style-bullet text:level="1" text:bullet-char="●">
      <style:list-level-properties text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="2" text:bullet-char="●">
      <style:list-level-properties text:space-before="0.6cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="3" text:bullet-char="●">
      <style:list-level-properties text:space-before="1.2cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="4" text:bullet-char="●">
      <style:list-level-properties text:space-before="1.8cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="5" text:bullet-char="●">
      <style:list-level-properties text:space-before="2.4cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="6" text:bullet-char="●">
      <style:list-level-properties text:space-before="3cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="7" text:bullet-char="●">
      <style:list-level-properties text:space-before="3.6cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="8" text:bullet-char="●">
      <style:list-level-properties text:space-before="4.2cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="9" text:bullet-char="●">
      <style:list-level-properties text:space-before="4.8cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
     <text:list-level-style-bullet text:level="10" text:bullet-char="●">
      <style:list-level-properties text:space-before="5.4cm" text:min-label-width="0.6cm"/>
      <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
     </text:list-level-style-bullet>
    </text:list-style>
   </style:graphic-properties>
   <style:paragraph-properties fo:margin-left="0cm" fo:margin-right="0cm" fo:margin-top="0cm" fo:margin-bottom="0cm" fo:line-height="100%" fo:text-indent="0cm"/>
   <style:text-properties fo:font-variant="normal" fo:text-transform="none" style:use-window-font-color="true" loext:opacity="0%" style:text-outline="false" style:text-line-through-style="none" style:text-line-through-type="none" style:font-name="Liberation Sans" fo:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable" fo:font-size="18pt" fo:font-style="normal" fo:text-shadow="none" style:text-underline-style="none" fo:font-weight="normal" style:letter-kerning="true" style:font-name-asian="Noto Sans CJK SC" style:font-family-asian="&apos;Noto Sans CJK SC&apos;" style:font-family-generic-asian="system" style:font-pitch-asian="variable" style:font-size-asian="18pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-name-complex="Lohit Devanagari" style:font-family-complex="&apos;Lohit Devanagari&apos;" style:font-family-generic-complex="system" style:font-pitch-complex="variable" style:font-size-complex="18pt" style:font-style-complex="normal" style:font-weight-complex="normal" style:text-emphasize="none" style:font-relief="none" style:text-overline-style="none" style:text-overline-color="font-color"/>
  </style:style>
  <style:style style:name="objectwithoutfill" style:family="graphic" style:parent-style-name="standard">
   <style:graphic-properties draw:fill="none"/>
  </style:style>
  <style:style style:name="Object_20_with_20_no_20_fill_20_and_20_no_20_line" style:display-name="Object with no fill and no line" style:family="graphic" style:parent-style-name="standard">
   <style:graphic-properties draw:stroke="none" draw:fill="none"/>
  </style:style>
  <style:style style:name="Text" style:family="graphic">
   <style:graphic-properties draw:stroke="solid" svg:stroke-color="#cccccc" draw:fill="solid" draw:fill-color="#eeeeee"/>
   <style:text-properties style:font-name="Noto Sans" fo:font-family="&apos;Noto Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  </style:style>
  <style:style style:name="A4" style:family="graphic" style:parent-style-name="Text">
   <style:graphic-properties draw:fill="none"/>
   <style:text-properties fo:font-size="18pt"/>
  </style:style>
  <style:style style:name="Title_20_A4" style:display-name="Title A4" style:family="graphic" style:parent-style-name="A4">
   <style:graphic-properties draw:stroke="none"/>
   <style:text-properties fo:font-size="44pt"/>
  </style:style>
  <style:style style:name="Heading_20_A4" style:display-name="Heading A4" style:family="graphic" style:parent-style-name="A4">
   <style:graphic-properties draw:stroke="none"/>
   <style:text-properties fo:font-size="24pt"/>
  </style:style>
  <style:style style:name="Text_20_A4" style:display-name="Text A4" style:family="graphic" style:parent-style-name="A4">
   <style:graphic-properties draw:stroke="none"/>
  </style:style>
  <style:style style:name="A4" style:family="graphic" style:parent-style-name="Text">
   <style:graphic-properties draw:fill="none"/>
   <style:text-properties fo:font-size="18pt"/>
  </style:style>
  <style:style style:name="Title_20_A0" style:display-name="Title A0" style:family="graphic" style:parent-style-name="A4">
   <style:graphic-properties draw:stroke="none"/>
   <style:text-properties fo:font-size="96pt"/>
  </style:style>
  <style:style style:name="Heading_20_A0" style:display-name="Heading A0" style:family="graphic" style:parent-style-name="A4">
   <style:graphic-properties draw:stroke="none"/>
   <style:text-properties fo:font-size="71.9000015258789pt"/>
  </style:style>
  <style:style style:name="Text_20_A0" style:display-name="Text A0" style:family="graphic" style:parent-style-name="A4">
   <style:graphic-properties draw:stroke="none"/>
  </style:style>
  <style:style style:name="Graphic" style:family="graphic">
   <style:graphic-properties draw:fill="solid" draw:fill-color="#ffffff"/>
   <style:text-properties style:font-name="Liberation Sans" fo:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable" fo:font-size="18pt"/>
  </style:style>
  <style:style style:name="Shapes" style:family="graphic" style:parent-style-name="Graphic">
   <style:graphic-properties draw:stroke="none" draw:fill="gradient" draw:fill-gradient-name="Shapes"/>
   <style:text-properties fo:font-size="14pt" fo:font-weight="bold"/>
  </style:style>
  <style:style style:name="Filled" style:family="graphic" style:parent-style-name="Shapes">
   <style:graphic-properties draw:fill="gradient" draw:fill-gradient-name="Filled"/>
  </style:style>
  <style:style style:name="Filled_20_Blue" style:display-name="Filled Blue" style:family="graphic" style:parent-style-name="Filled">
   <style:graphic-properties draw:fill-gradient-name="Filled_20_Blue"/>
   <style:text-properties fo:color="#ffffff" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Filled_20_Green" style:display-name="Filled Green" style:family="graphic" style:parent-style-name="Filled">
   <style:graphic-properties draw:fill-gradient-name="Filled_20_Green"/>
   <style:text-properties fo:color="#ffffff" loext:opacity="100%" style:font-name="Liberation Sans" fo:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  </style:style>
  <style:style style:name="Filled_20_Red" style:display-name="Filled Red" style:family="graphic" style:parent-style-name="Filled">
   <style:graphic-properties draw:fill-gradient-name="Filled_20_Red"/>
   <style:text-properties fo:color="#ffffff" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Filled_20_Yellow" style:display-name="Filled Yellow" style:family="graphic" style:parent-style-name="Filled">
   <style:graphic-properties draw:fill-gradient-name="Filled_20_Yellow"/>
   <style:text-properties fo:color="#ffffff" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Outlined" style:family="graphic" style:parent-style-name="Shapes">
   <style:graphic-properties draw:stroke="solid" svg:stroke-width="0.081cm" svg:stroke-color="#000000" draw:fill="none"/>
  </style:style>
  <style:style style:name="Outlined_20_Blue" style:display-name="Outlined Blue" style:family="graphic" style:parent-style-name="Outlined">
   <style:graphic-properties svg:stroke-color="#355269"/>
   <style:text-properties fo:color="#355269" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Outlined_20_Green" style:display-name="Outlined Green" style:family="graphic" style:parent-style-name="Outlined">
   <style:graphic-properties svg:stroke-color="#127622"/>
   <style:text-properties fo:color="#127622" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Outlined_20_Red" style:display-name="Outlined Red" style:family="graphic" style:parent-style-name="Outlined">
   <style:graphic-properties svg:stroke-color="#c9211e"/>
   <style:text-properties fo:color="#c9211e" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Outlined_20_Yellow" style:display-name="Outlined Yellow" style:family="graphic" style:parent-style-name="Outlined">
   <style:graphic-properties draw:stroke="solid" svg:stroke-color="#b47804"/>
   <style:text-properties fo:color="#b47804" loext:opacity="100%"/>
  </style:style>
  <style:style style:name="Lines" style:family="graphic" style:parent-style-name="Graphic">
   <style:graphic-properties draw:stroke="solid" svg:stroke-color="#000000" draw:fill="none"/>
  </style:style>
  <style:style style:name="Arrow_20_Line" style:display-name="Arrow Line" style:family="graphic" style:parent-style-name="Lines">
   <style:graphic-properties draw:marker-start="Arrow" draw:marker-start-width="0.2cm" draw:marker-end="Arrow" draw:marker-end-width="0.2cm" draw:show-unit="true"/>
  </style:style>
  <style:style style:name="Arrow_20_Dashed" style:display-name="Arrow Dashed" style:family="graphic" style:parent-style-name="Lines">
   <style:graphic-properties draw:stroke="dash"/>
  </style:style>
 </office:styles>
 <office:automatic-styles>
  <style:page-layout style:name="PM0">
   <style:page-layout-properties fo:margin-top="0.635cm" fo:margin-bottom="0.635cm" fo:margin-left="0.635cm" fo:margin-right="0.635cm" fo:page-width="21.59cm" fo:page-height="27.94cm" style:print-orientation="portrait"/>
  </style:page-layout>
  <style:style style:name="dp1" style:family="drawing-page">
   <style:drawing-page-properties draw:background-size="border" draw:fill="none"/>
  </style:style>
  <style:style style:name="dp2" style:family="drawing-page"/>
  <style:style style:name="gr1" style:family="graphic" style:parent-style-name="standard">
   <style:graphic-properties draw:stroke="none" svg:stroke-color="#666666" draw:fill="solid" draw:fill-color="#eeeeee" draw:textarea-horizontal-align="justify" draw:textarea-vertical-align="middle" draw:auto-grow-height="false" fo:min-height="1.184cm" fo:min-width="0.933cm"/>
  </style:style>
  <style:style style:name="gr2" style:family="graphic" style:parent-style-name="standard">
   <style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-horizontal-align="justify" draw:textarea-vertical-align="middle" draw:auto-grow-height="false" fo:min-height="1.851cm" fo:min-width="6.25cm"/>
   <style:paragraph-properties style:writing-mode="lr-tb"/>
  </style:style>
  <style:style style:name="gr3" style:family="graphic" style:parent-style-name="standard">
   <style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-horizontal-align="justify" draw:textarea-vertical-align="middle" draw:auto-grow-height="false" fo:min-height="1.338cm" fo:min-width="4.6cm"/>
   <style:paragraph-properties style:writing-mode="lr-tb"/>
  </style:style>
  <style:style style:name="gr4" style:family="graphic" style:parent-style-name="objectwithoutfill">
   <style:graphic-properties svg:stroke-width="0.081cm" svg:stroke-color="#dddddd" draw:marker-start-width="0.321cm" draw:marker-end-width="0.321cm" svg:stroke-linecap="round" draw:fill="none" draw:textarea-vertical-align="middle" fo:padding-top="0.165cm" fo:padding-bottom="0.165cm" fo:padding-left="0.29cm" fo:padding-right="0.29cm"/>
  </style:style>
  <style:style style:name="gr5" style:family="graphic" style:parent-style-name="objectwithoutfill">
   <style:graphic-properties svg:stroke-color="#000000" draw:fill="none" draw:textarea-vertical-align="middle"/>
  </style:style>
  <style:style style:name="gr6" style:family="graphic" style:parent-style-name="Object_20_with_20_no_20_fill_20_and_20_no_20_line">
   <style:graphic-properties draw:stroke="none" draw:fill="none" draw:textarea-horizontal-align="center" draw:textarea-vertical-align="middle" draw:color-mode="standard" draw:luminance="0%" draw:contrast="0%" draw:gamma="100%" draw:red="0%" draw:green="0%" draw:blue="0%" fo:clip="rect(0cm, 0cm, 0cm, 0cm)" draw:image-opacity="100%" style:mirror="none"/>
  </style:style>
  <style:style style:name="P1" style:family="paragraph">
   <loext:graphic-properties draw:fill="solid" draw:fill-color="#eeeeee"/>
   <style:paragraph-properties fo:text-align="center"/>
  </style:style>
  <style:style style:name="P2" style:family="paragraph">
   <style:paragraph-properties fo:text-align="center" style:writing-mode="lr-tb"/>
   <style:text-properties style:font-name="DejaVu Sans" fo:font-size="24pt"/>
  </style:style>
  <style:style style:name="P3" style:family="paragraph">
   <loext:graphic-properties draw:fill="none"/>
   <style:paragraph-properties fo:text-align="center" style:writing-mode="lr-tb"/>
   <style:text-properties style:font-name="DejaVu Sans" fo:font-size="24pt"/>
  </style:style>
  <style:style style:name="P4" style:family="paragraph">
   <style:paragraph-properties fo:text-align="center" style:writing-mode="lr-tb"/>
   <style:text-properties fo:color="#666666" loext:opacity="100%" style:font-name="DejaVu Sans" fo:font-size="18pt" fo:font-style="italic" style:font-size-asian="18pt" style:font-size-complex="18pt"/>
  </style:style>
  <style:style style:name="P5" style:family="paragraph">
   <loext:graphic-properties draw:fill="none"/>
   <style:paragraph-properties fo:text-align="center" style:writing-mode="lr-tb"/>
   <style:text-properties fo:color="#666666" loext:opacity="100%" style:font-name="DejaVu Sans" fo:font-size="18pt" fo:font-style="italic" style:font-size-asian="18pt" style:font-size-complex="18pt"/>
  </style:style>
  <style:style style:name="P6" style:family="paragraph">
   <loext:graphic-properties draw:fill="none"/>
   <style:paragraph-properties fo:text-align="center"/>
  </style:style>
  <style:style style:name="T1" style:family="text">
   <style:text-properties style:font-name="DejaVu Sans" fo:font-size="24pt"/>
  </style:style>
  <style:style style:name="T2" style:family="text">
   <style:text-properties fo:color="#666666" loext:opacity="100%" style:font-name="DejaVu Sans" fo:font-size="18pt" fo:font-style="italic" style:font-size-asian="18pt" style:font-size-complex="18pt"/>
  </style:style>
  <text:list-style style:name="L1">
   <text:list-level-style-bullet text:level="1" text:bullet-char="●">
    <style:list-level-properties text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="2" text:bullet-char="●">
    <style:list-level-properties text:space-before="0.6cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="3" text:bullet-char="●">
    <style:list-level-properties text:space-before="1.2cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="4" text:bullet-char="●">
    <style:list-level-properties text:space-before="1.8cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="5" text:bullet-char="●">
    <style:list-level-properties text:space-before="2.4cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="6" text:bullet-char="●">
    <style:list-level-properties text:space-before="3cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="7" text:bullet-char="●">
    <style:list-level-properties text:space-before="3.6cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="8" text:bullet-char="●">
    <style:list-level-properties text:space-before="4.2cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="9" text:bullet-char="●">
    <style:list-level-properties text:space-before="4.8cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
   <text:list-level-style-bullet text:level="10" text:bullet-char="●">
    <style:list-level-properties text:space-before="5.4cm" text:min-label-width="0.6cm"/>
    <style:text-properties fo:font-family="StarSymbol" style:use-window-font-color="true" fo:font-size="45%"/>
   </text:list-level-style-bullet>
  </text:list-style>
 </office:automatic-styles>
 <office:master-styles>
  <draw:layer-set>
   <draw:layer draw:name="layout"/>
   <draw:layer draw:name="background"/>
   <draw:layer draw:name="backgroundobjects"/>
   <draw:layer draw:name="controls"/>
   <draw:layer draw:name="measurelines"/>
  </draw:layer-set>
  <style:master-page style:name="Default" style:page-layout-name="PM0" draw:style-name="dp1"/>
 </office:master-styles>
 <office:body>
  <office:drawing>
"""


# In[87]:


page_intro = """   <draw:page draw:name="page1" draw:style-name="dp2" draw:master-page-name="Default">"""


# In[88]:


group_template="""    <draw:g>
     <draw:custom-shape draw:style-name="gr1" draw:text-style-name="P1" draw:layer="layout" svg:width="1.587cm" svg:height="1.588cm" svg:x="5.635cm" svg:y="1.435cm">
      <text:p/>
      <draw:enhanced-geometry svg:viewBox="0 0 21600 21600" draw:mirror-horizontal="false" draw:mirror-vertical="false" draw:path-stretchpoint-x="10800" draw:path-stretchpoint-y="10800" draw:text-areas="?f3 ?f4 ?f5 ?f6" draw:type="round-rectangle" draw:modifiers="3600" draw:enhanced-path="M ?f7 0 X 0 ?f8 L 0 ?f9 Y ?f7 21600 L ?f10 21600 X 21600 ?f9 L 21600 ?f8 Y ?f10 0 Z N">
       <draw:equation draw:name="f0" draw:formula="45"/>
       <draw:equation draw:name="f1" draw:formula="$0 *sin(?f0 *(pi/180))"/>
       <draw:equation draw:name="f2" draw:formula="?f1 *3163/7636"/>
       <draw:equation draw:name="f3" draw:formula="left+?f2 "/>
       <draw:equation draw:name="f4" draw:formula="top+?f2 "/>
       <draw:equation draw:name="f5" draw:formula="right-?f2 "/>
       <draw:equation draw:name="f6" draw:formula="bottom-?f2 "/>
       <draw:equation draw:name="f7" draw:formula="left+$0 "/>
       <draw:equation draw:name="f8" draw:formula="top+$0 "/>
       <draw:equation draw:name="f9" draw:formula="bottom-$0 "/>
       <draw:equation draw:name="f10" draw:formula="right-$0 "/>
       <draw:handle draw:handle-position="$0 top" draw:handle-switched="true" draw:handle-range-x-minimum="0" draw:handle-range-x-maximum="10800"/>
      </draw:enhanced-geometry>
     </draw:custom-shape>
     <draw:custom-shape draw:style-name="gr2" draw:text-style-name="P3" draw:layer="layout" svg:width="6.75cm" svg:height="2.101cm" svg:x="0.635cm" svg:y="2.857cm">
      <text:p text:style-name="P2"><text:span text:style-name="T1">SUFGANIYOT</text:span></text:p>
      <draw:enhanced-geometry svg:viewBox="0 0 21600 21600" draw:type="rectangle" draw:enhanced-path="M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N"/>
     </draw:custom-shape>
     <draw:custom-shape draw:style-name="gr3" draw:text-style-name="P5" draw:layer="layout" svg:width="5.1cm" svg:height="1.588cm" draw:transform="rotate (-3.14159265358979) translate (5.735cm 2.858cm)">
      <text:p text:style-name="P4"><text:span text:style-name="T2">SUFGANIYOT</text:span></text:p>
      <draw:enhanced-geometry svg:viewBox="0 0 21600 21600" draw:type="rectangle" draw:enhanced-path="M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N"/>
     </draw:custom-shape>
     <draw:line draw:style-name="gr4" draw:text-style-name="P6" draw:layer="layout" svg:x1="0.952cm" svg:y1="2.857cm" svg:x2="5.397cm" svg:y2="2.857cm">
      <text:p/>
     </draw:line>
     <draw:g draw:name="corner">
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="0.635cm" svg:y1="0.635cm" svg:x2="0.953cm" svg:y2="0.635cm">
       <text:p/>
      </draw:line>
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="0.635cm" svg:y1="0.953cm" svg:x2="0.635cm" svg:y2="0.635cm">
       <text:p/>
      </draw:line>
     </draw:g>
     <draw:g draw:name="corner 1">
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="0.635cm" svg:y1="5.035cm" svg:x2="0.635cm" svg:y2="4.717cm">
       <text:p/>
      </draw:line>
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="0.953cm" svg:y1="5.035cm" svg:x2="0.635cm" svg:y2="5.035cm">
       <text:p/>
      </draw:line>
     </draw:g>
     <draw:g draw:name="corner 3">
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="7.385cm" svg:y1="0.635cm" svg:x2="7.385cm" svg:y2="0.953cm">
       <text:p/>
      </draw:line>
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="7.067cm" svg:y1="0.635cm" svg:x2="7.385cm" svg:y2="0.635cm">
       <text:p/>
      </draw:line>
     </draw:g>
     <draw:g draw:name="corner 2">
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="7.385cm" svg:y1="5.035cm" svg:x2="7.067cm" svg:y2="5.035cm">
       <text:p/>
      </draw:line>
      <draw:line draw:style-name="gr5" draw:text-style-name="P6" draw:layer="layout" svg:x1="7.385cm" svg:y1="4.717cm" svg:x2="7.385cm" svg:y2="5.035cm">
       <text:p/>
      </draw:line>
     </draw:g>
     <draw:frame draw:style-name="gr6" draw:text-style-name="P6" draw:layer="layout" svg:width="1.019cm" svg:height="1.176cm" svg:x="5.92cm" svg:y="1.641cm">
      <draw:image draw:mime-type="image/svg+xml">
       <office:binary-data>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+
        CjxzdmcKICAgdmVyc2lvbj0iMS4wIgogICB3aWR0aD0iMTEwOS4wMDAwMDBwdCIKICAgaGVp
        Z2h0PSIxMjgwLjAwMDAwMHB0IgogICB2aWV3Qm94PSIwIDAgMTEwOS4wMDAwMDAgMTI4MC4w
        MDAwMDAiCiAgIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIG1lZXQiCiAgIGlkPSJz
        dmcxOCIKICAgc29kaXBvZGk6ZG9jbmFtZT0ieURoclFELnN2ZyIKICAgaW5rc2NhcGU6dmVy
        c2lvbj0iMS4xLjIgKDBhMDBjZjUzMzksIDIwMjItMDItMDQpIgogICB4bWxuczppbmtzY2Fw
        ZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgeG1s
        bnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlw
        b2RpLTAuZHRkIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHht
        bG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9
        ImRlZnMyMiIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzIw
        IgogICAgIHBhZ2Vjb2xvcj0iI2ZmZmZmZiIKICAgICBib3JkZXJjb2xvcj0iIzY2NjY2NiIK
        ICAgICBib3JkZXJvcGFjaXR5PSIxLjAiCiAgICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIK
        ICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VjaGVj
        a2VyYm9hcmQ9IjAiCiAgICAgaW5rc2NhcGU6ZG9jdW1lbnQtdW5pdHM9InB0IgogICAgIHNo
        b3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSIwLjUyMjA3MDMxIgogICAgIGlu
        a3NjYXBlOmN4PSI3MzguNDA2MjkiCiAgICAgaW5rc2NhcGU6Y3k9Ijg1My4zMzMzMyIKICAg
        ICBpbmtzY2FwZTp3aW5kb3ctd2lkdGg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LWhl
        aWdodD0iMTA1MiIKICAgICBpbmtzY2FwZTp3aW5kb3cteD0iMTkyMCIKICAgICBpbmtzY2Fw
        ZTp3aW5kb3cteT0iMCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIxIgogICAg
        IGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9ImcxNiIgLz4KICA8bWV0YWRhdGEKICAgICBpZD0i
        bWV0YWRhdGEyIj4KQ3JlYXRlZCBieSBwb3RyYWNlIDEuMTUsIHdyaXR0ZW4gYnkgUGV0ZXIg
        U2VsaW5nZXIgMjAwMS0yMDE3CjwvbWV0YWRhdGE+CiAgPGcKICAgICB0cmFuc2Zvcm09Im1h
        dHJpeCgwLjEsMCwwLC0wLjEsMCwxMjgwKSIKICAgICBmaWxsPSIjMDAwMDAwIgogICAgIHN0
        cm9rZT0ibm9uZSIKICAgICBpZD0iZzE2Ij4KICAgIDxwYXRoCiAgICAgICBkPSJNIDUxMzMs
        MTIwODcgQyA0OTA3LDExNjk1IDQyMDYsMTA0ODIgMzU3NSw5MzkwIDI5MjUsODI2MyAyNDMx
        LDczOTggMjQzMyw3Mzg5IGMgNiwtMjIgNDgwLC04NDggNDg4LC04NDkgMywwIDU5NCwxMDE5
        IDEzMTQsMjI2NSA3MTksMTI0NiAxMzEwLDIyNjMgMTMxMywyMjYxIDIsLTMgMTc3LC0zMDQg
        Mzg3LC02NjggbCAzODMsLTY2MyA0OTcsLTMgYyA0NDksLTIgNDk3LC0xIDQ5MSwxNCAtNSwx
        MyAtMTcwMCwyOTU0IC0xNzQ1LDMwMjYgbCAtMTYsMjcgeiIKICAgICAgIGlkPSJwYXRoNCIK
        ICAgICAgIHN0eWxlPSJzdHJva2U6bm9uZTtmaWxsOiM2NjY2NjY7ZmlsbC1vcGFjaXR5OjEi
        IC8+CiAgICA8cGF0aAogICAgICAgZD0ibSA5LDk1ODMgYyA2LC0xMCA3MDcsLTEyMjQgMTU1
        OSwtMjY5OCBsIDE1NDgsLTI2ODAgNDk3LC0zIGMgMjczLC0xIDQ5NywwIDQ5NywzIDAsMyAt
        NTg3LDEwMjMgLTEzMDUsMjI2NSAtNzE4LDEyNDMgLTEzMDUsMjI2MiAtMTMwNSwyMjY1IDAs
        MyAzNDgsNSA3NzMsNSBoIDc3NCBsIDI0Myw0MjMgYyAxMzQsMjMyIDI0NSw0MjUgMjQ3LDQz
        MCAyLDQgLTc5Myw3IC0xNzY3LDcgQyA4Nyw5NjAwIDAsOTU5OSA5LDk1ODMgWiIKICAgICAg
        IGlkPSJwYXRoNiIKICAgICAgIHN0eWxlPSJzdHJva2U6bm9uZTtmaWxsOiM2NjY2NjY7Zmls
        bC1vcGFjaXR5OjEiIC8+CiAgICA8cGF0aAogICAgICAgZD0ibSA0NTk5LDkxNzIgLTI0Niwt
        NDI3IDI2MjAsLTMgYyAyMDg4LC0yIDI2MTgsLTUgMjYxNCwtMTUgLTMsLTYgLTE3NiwtMzA5
        IC0zODYsLTY3MSBsIC0zODEsLTY2MCA4MSwtMTQwIGMgNDUsLTc4IDE1NiwtMjcwIDI0Nywt
        NDI4IDkxLC0xNTkgMTY4LC0yODggMTcxLC0yODggMywxIDM5Myw2NzIgODY2LDE0OTIgNDcz
        LDgyMCA4NzAsMTUwOCA4ODMsMTUyOSBsIDIzLDM5IEggNzk2OCBsIC0zMTIzLC0xIHoiCiAg
        ICAgICBpZD0icGF0aDgiCiAgICAgICBzdHlsZT0ic3Ryb2tlOm5vbmU7ZmlsbDojNjY2NjY2
        O2ZpbGwtb3BhY2l0eToxIiAvPgogICAgPHBhdGgKICAgICAgIGQ9Im0gNjk4MCw4NTk1IGMg
        MCwtMyA2NywtMTIxIDE0OSwtMjYzIDEyMTksLTIxMDkgMjQ2MSwtNDI2MiAyNDYxLC00MjY3
        IDAsLTMgLTM0OCwtNSAtNzczLC01IGggLTc3NCBsIC0yNDYsLTQyNyAtMjQ3LC00MjggODg1
        LC0zIGMgNDg3LC0xIDEyODMsLTEgMTc2OSwwIGwgODgzLDMgLTEwMTksMTc2NSBDIDk1MDcs
        NTk0MSA4ODA2LDcxNTQgODUxMSw3NjY1IGwgLTUzNyw5MzAgLTQ5NywzIGMgLTI3MywxIC00
        OTcsMCAtNDk3LC0zIHoiCiAgICAgICBpZD0icGF0aDEwIgogICAgICAgc3R5bGU9InN0cm9r
        ZTpub25lO2ZpbGw6IzY2NjY2NjtmaWxsLW9wYWNpdHk6MSIgLz4KICAgIDxwYXRoCiAgICAg
        ICBkPSJNIDkwNSw0NzY4IEMgNDMyLDM5NDggMzUsMzI2MCAyMiwzMjM5IGwgLTIzLC0zOSBo
        IDMxMjMgbCAzMTIzLDEgMjQ2LDQyNyAyNDYsNDI3IC0yNjIwLDMgYyAtMjA4OCwyIC0yNjE4
        LDUgLTI2MTQsMTUgMyw2IDE3NiwzMDkgMzg2LDY3MSBsIDM4MSw2NjAgLTk4LDE3MCBjIC0z
        MDksNTM3IC0zOTYsNjg2IC00MDEsNjg2IC0zLC0xIC0zOTMsLTY3MiAtODY2LC0xNDkyIHoi
        CiAgICAgICBpZD0icGF0aDEyIgogICAgICAgc3R5bGU9InN0cm9rZTpub25lO2ZpbGw6IzY2
        NjY2NjtmaWxsLW9wYWNpdHk6MSIgLz4KICAgIDxwYXRoCiAgICAgICBkPSJNIDY4NTUsMzk5
        NSBDIDYxMzYsMjc0OSA1NTQ1LDE3MzIgNTU0MiwxNzM0IGMgLTIsMyAtMTc3LDMwMyAtMzg3
        LDY2OCBsIC0zODMsNjYzIC00OTcsMyBjIC00NDksMiAtNDk3LDEgLTQ5MSwtMTQgNSwtMTMg
        MTcwMSwtMjk1NCAxNzQ1LC0zMDI2IGwgMTcsLTI3IDI4MSw0ODcgYyAxNTQsMjY4IDg1Niwx
        NDgyIDE1NTgsMjY5NyAxMDc5LDE4NjkgMTI3NSwyMjE0IDEyNjgsMjIzMyAtMTEsMzIgLTQ3
        Nyw4NDEgLTQ4NCw4NDIgLTMsMCAtNTk0LC0xMDE5IC0xMzE0LC0yMjY1IHoiCiAgICAgICBp
        ZD0icGF0aDE0IgogICAgICAgc3R5bGU9InN0cm9rZTpub25lO2ZpbGw6IzY2NjY2NjtmaWxs
        LW9wYWNpdHk6MSIgLz4KICA8L2c+Cjwvc3ZnPgo=
       </office:binary-data>
       <text:p/>
      </draw:image>
     </draw:frame>
    </draw:g>"""


# In[89]:


page_outro = """   </draw:page>
"""


# In[90]:


tail_matter="""  </office:drawing>
 </office:body>
</office:document>"""


# In[91]:


def find_all_x_location_text(txt):
    items = []
    items += re.findall('x="\S*cm"', txt)
    items += re.findall('x1="\S*cm"', txt)
    items += re.findall('x2="\S*cm"', txt)
    return sorted(list(set(items)), reverse=True)
def find_all_y_location_text(txt):
    items = []
    items += re.findall('y="\S*cm"', txt)
    items += re.findall('y1="\S*cm"', txt)
    items += re.findall('y2="\S*cm"', txt)
    return sorted(list(set(items)), reverse=True)


# In[92]:


def find_all_translation_text(txt):
    return re.findall('translate\s\(\S*\s\S*\)',txt)


# In[93]:


def extract_x_and_y_from_translation_text(txt):
    # from output in find_all_translation_text, finds the x and y values as str
    return re.findall('\d*\.\d*',txt)


# In[94]:


def extract_number_from_spec(txt):
    # extracts number from input text like 'x="5.635cm"'
    # returns a string
    return re.findall('\d*\.\d*',txt)[0] #this can be made more efficient and robust


# In[95]:


def move_group(group_text, row_num=0, col_num=0, row_sep=4.4, col_sep=6.75):
    updated_group_text = group_text
    if col_num > 0:
        shift = col_num * col_sep
        specs_to_update = find_all_x_location_text(group_text)
        for spec in specs_to_update:
            num_str = extract_number_from_spec(spec)
            new_num = str(float(num_str) + shift)
            new_spec = re.sub(num_str, new_num, spec)
            updated_group_text = re.sub(spec, new_spec, updated_group_text)
        translation_texts = find_all_translation_text(updated_group_text)
        for txt in translation_texts:
            num_str = extract_x_and_y_from_translation_text(txt)[0]
            new_num = str(float(num_str) + shift)
            new_spec = re.sub(num_str, new_num, txt)
            updated_group_text = re.sub(re.escape(txt), new_spec, updated_group_text)
    if row_num > 0:
        shift = row_num * row_sep
        specs_to_update = find_all_y_location_text(group_text)
        for spec in specs_to_update:
            num_str = extract_number_from_spec(spec)
            new_num = str(float(num_str) + shift)
            new_spec = re.sub(num_str, new_num, spec)
            updated_group_text = re.sub(spec, new_spec, updated_group_text)
        translation_texts = find_all_translation_text(updated_group_text)
        for txt in translation_texts:
            num_str = extract_x_and_y_from_translation_text(txt)[1]
            new_num = str(float(num_str) + shift)
            new_spec = re.sub(num_str, new_num, txt)
            updated_group_text = re.sub(re.escape(txt), new_spec, updated_group_text)
    return updated_group_text
            


# In[96]:


def replace_text_in_group(group_text, word):
    return re.sub('SUFGANIYOT',word.upper(),group_text)


# In[97]:


f = open('words.txt', 'r')
words = f.read().splitlines()
f.close()


# In[98]:


document = head_matter + page_intro


# In[99]:


row = 0
col = 0
for word in words:
    new_word_group = replace_text_in_group(group_template, word)
    shifted_group = move_group(new_word_group, row_num=row, col_num=col)
    document += shifted_group
    col += 1
    if col == 3:
        row += 1
        col = 0
    if row == 6:
        row = 0
        col = 0
        document += page_outro + page_intro


# In[100]:


document += page_outro + tail_matter


# In[101]:


f = open('codenames_cards.fodg', 'w')
f.write(document)
f.close()
